from django.shortcuts import render

def permission_denied_view(request):
    template_name = "error/permission_denied.html"
    return render(request, template_name, {})
