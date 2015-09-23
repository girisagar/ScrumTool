from django.views.generic import TemplateView
from django.shortcuts import render

from scrum.models.sprint import Sprint
from scrum.models.work_log import WorkLog
from scrum.models.user_story import UserStory
from scrum.models.release_backlog import ReleaseBacklog

import datetime


# class SprintBurndownChartView(TemplateView):
#     template_name = "about.html"

#    def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello, World!')


def sprint(request, pk):
    # days = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6',
    #         'Day7', 'Day8', 'Day9', 'Day10', 'Day11']
    # ideal_data = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    # actual_data = [100, 90, 85, 60, 60, 30, 32, 23, 9, 2, 5]
    
    # context = { "days": days,
    #             "ideal_data": ideal_data,
    #             "actual_data": actual_data
    # }

    if request.method == "POST":
        if "sprint" in request.POST:
            sprint_name = request.POST["sprint"]
        else:
            sprint_name = get_latest_sprint()
    elif request.method == "GET":
        sprint_name = get_latest_sprint()
    
    release_backlogs = get_backlogs(pk)

    sprint = Sprint.objects.filter(product_backlog_id=pk, name=sprint_name).get()
    sprint_id = sprint.id
    if sprint.sprint_start:
        sprint_start = str(sprint.sprint_start.date())
        user_stories = UserStory.objects.filter(sprint=sprint_id)

        user_story_list = []
        for user_story in user_stories:
            user_story_list.append(user_story.id)

        print "User story ids: ", user_story_list

        date_list = sprint_frmto(sprint_start)

        burndown_chart = {}

        for date in date_list:
            burndown_chart[date] = 0

        for date in date_list:
            print "date: ", date
            for user_story_id in user_story_list:
                # print "user story id: ", user_story_id 
                for worklog in WorkLog.objects.filter(user_story_id=user_story_id, date=date):
                    # print "worklog id: ", worklog.id, " work_reamaingin: ", worklog.work_remaining
                    burndown_chart[date] = burndown_chart[date] + worklog.work_remaining
                # print "total_work_remaining: ", burndown_chart[date]
                # print "================="
            # print "---------------------------------"
        sorted_burndown_chart = sorted(burndown_chart.items(), key=lambda x: x[0])

        days = [i[0]  for i in sorted_burndown_chart]
        actual_data = [j[1] for j in sorted_burndown_chart]
        
        context = { "days": days,
                    "actual_data": actual_data,
                    "sprint_name": sprint_name,
                    "release_backlogs": release_backlogs,
        }
    else:
        context = { 
                    "days": ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7'],
                    "actual_data": [0, 0, 0, 0, 0, 0, 0],
                    "sprint_name": sprint_name + " yet to start !!!",
                    "release_backlogs": release_backlogs,
        }



    return render(request, "burndownchart.html", context)

def sprint_frmto(sprint_started):
    sprint_started = '2015-09-21' # from db
    frm_date = datetime.datetime.strptime(sprint_started, "%Y-%m-%d").date()
    to_date = datetime.datetime.strptime("2015-09-24", "%Y-%m-%d").date()
    # to_date = datetime.datetime.today().date()
    days = (to_date - frm_date).days

    date_list = []
    for interval in range(days+1):
        date_list.append(str(frm_date + datetime.timedelta(days=interval)))
    return date_list

def get_backlogs(product_backlog_id=1):
    release_backlogs ={}

    for release_backlog in ReleaseBacklog.objects.filter(product_backlog=product_backlog_id):
        release_backlogs[release_backlog.name] = {"id": release_backlog.id, "sprints": []}
        for sprint in Sprint.objects.filter(release_backlog=release_backlog.id):
            release_backlogs[release_backlog.name]["sprints"].append(sprint.name)
    return release_backlogs

def get_latest_sprint():
    return  Sprint.objects.latest('sprint_start').name
