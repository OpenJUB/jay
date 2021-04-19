from django.conf.urls import url
from allauth.socialaccount import views

urlpatterns = [
    url('^login/cancelled/$', views.login_cancelled,
        name='socialaccount_login_cancelled'),
    url('^login/error/$', views.login_error, name='socialaccount_login_error')
]
