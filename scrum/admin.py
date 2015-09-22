from django.contrib import admin
from scrum.models import (
	ProductBacklog,
	ReleaseBacklog,
	UserStory,
	WorkLog,
	Sprint
)

class UserStoryAdmin(admin.ModelAdmin):
	list_display = ('title', 
					'assiged_developer', 'developer_effort',
					'assiged_tester', 'tester_effort',
					'sprint')

class WorkLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'user_story', "work_done", "work_remaining", "employee")

class SprintAdmin(admin.ModelAdmin):
	list_display =('name', 'release_backlog', 'sprint_start', 'sprint_end')

admin.site.register(ProductBacklog)
admin.site.register(ReleaseBacklog)
admin.site.register(UserStory, UserStoryAdmin)
admin.site.register(WorkLog, WorkLogAdmin)
admin.site.register(Sprint, SprintAdmin)