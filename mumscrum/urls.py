"""mumscrum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib.auth import login
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from mumscrum.views.page_not_found_view import page_not_found_view
from mumscrum.views.bad_request_view import bad_request_view
from mumscrum.views.permission_denied_view import permission_denied_view
from mumscrum.views.server_error_view import server_error_view

handler400 = bad_request_view
handler404 = page_not_found_view
handler403 = permission_denied_view
handler500 = server_error_view

urlpatterns = [
    url(
        r'^login/$',
        'hris.views.auth.login',
        {'template_name' : 'auth/login.html'},
        name='login'
    ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(
        r'^reset/$',
        password_reset,
        {'template_name' : 'auth/password_reset_form.html'},        
        name='password_reset',
    ),

    url(
        r'^reset/done/$',
        password_reset_done,
        {'template_name' : 'auth/password_reset_done.html'},
        name='password_reset_done'
    ),    

    url(
        r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, 
        {'post_reset_redirect' : '/reset/complete/', 
            'template_name' : 'auth/password_reset_confirm.html' },
        name="password_reset_confirm"
    ),

    url(
        r'^reset/complete/$',
        password_reset_complete,
        {'template_name' : 'auth/password_reset_complete.html' },
        name='password_reset_complete'
    ),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hris/', include("hris.urls")),
    url(r'^scrum/', include("scrum.urls")),
    url(r'^report/', include("report.urls")),
    url(r'^tasks/', include("emptask.urls")),
    url(r'^$', 'mumscrum.views.home', name='home'),
    # serving media files
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
    ]