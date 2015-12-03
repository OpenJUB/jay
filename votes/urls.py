from django.conf.urls import include, url

from django.views.generic import TemplateView

from votes.views import VoteView, results, system_home, system_settings, admin_add, admin_remove, vote_edit, vote_options_add, vote_options_edit, vote_options_remove

urlpatterns = [
    # Home for the votes
    url(r'^$', system_home, name="system"),

    # vote manager for a system
    url(r'^settings$', system_settings, name="settings"),

    # adding / removing admins
    url(r'^admins/add$', admin_add, name="admins_add"),
    url(r'^admins/remove$', admin_remove, name="admins_remove"),

    # vote and results
    url(r'^(?P<vote_name>[\w-]+)/$', VoteView.as_view(), name="vote"),
    url(r'^(?P<vote_name>[\w-]+)/results$', results, name="results"),

    # settings for a vote
    url(r'^(?P<vote_name>[\w-]+)/edit$', vote_edit, name="vote_edit"),

    # Options for a vote
    url(r'^(?P<vote_name>[\w-]+)/edit/options/add$', vote_options_add, name="vote_options_add"),
    url(r'^(?P<vote_name>[\w-]+)/edit/options/edit$', vote_options_edit, name="vote_options_edit"),
    url(r'^(?P<vote_name>[\w-]+)/edit/options/delete$', vote_options_remove, name="vote_options_delete"),
]
