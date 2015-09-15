from django.shortcuts import render

def bad_request_view(request):
    template_name = "error/bad_request.html"
    return request(request, template_name, {})