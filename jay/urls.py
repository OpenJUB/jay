"""jay URL Configuration

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
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView, RedirectView

from core.views import home

from votes import urls as votes_urls
from filters import urls as filters_urls
from settings import urls as settings_urls

urlpatterns = [
    # Home page
    url(r'^$', home, name="home"),

    # django admin
    url(r'^admin/', admin.site.urls),

    # Static stuff
    url(r'^imprint/$', RedirectView.as_view(url="https://jacobs-alumni.de/imprint"), name="imprint"),
    url(r'^privacy/$', RedirectView.as_view(url="https://jacobs-alumni.de/privacy"),
        name="privacy"),
    url(r'^about/$',
        TemplateView.as_view(template_name="base/humblebrag.html"),
        name="about"),
    url(r'^help/$', TemplateView.as_view(template_name="help/help.html"),
        name="help"),

    # Help
    url(r'^help/filters/$',
        TemplateView.as_view(template_name="filters/filter_help.html"),
        name="filter_help"),

    # Authentication
    url(r'^accounts/', include('jay.allauthurls.main'), name='login'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html', next_page='home'),
        name="logout"),

    # Sub-projects
    url(r'^filters/', include('filters.urls')),

    url(r'^settings/', include('settings.urls')),
    url(r'^(?P<system_name>[\w-]+)/', include('votes.urls')),
]
