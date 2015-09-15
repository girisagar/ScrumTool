from django.shortcuts import render

def page_not_found_view(request):
    template_name = "error/page_not_found.html"
    return render(request, template_name, {})