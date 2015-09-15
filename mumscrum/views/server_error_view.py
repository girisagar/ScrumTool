from django.shortcuts import render

def server_error_view(request):
    template_name = "error/server_error.html"
    return render(request, template_name, {})