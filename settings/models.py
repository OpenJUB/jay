from django.db import models

from django.contrib import admin

from jay.restricted import is_restricted_word
from jay.utils import is_superadmin
from users.models import Admin


class VotingSystem(models.Model):
    machine_name = models.SlugField(max_length=50, unique=True)
    simple_name = models.CharField(max_length=80)

    def __str__(self):
        return u'[%s] %s' % (self.machine_name, self.simple_name)

    def clean(self):
        is_restricted_word('machine_name', self.machine_name)

    def canEdit(self, user):
        """ Checks if a user can edit this voting system. """

        return is_superadmin(user)

    def isAdmin(self, user):
        """ Checks if a user is an administrator for this voting system. """
        if user.is_anonymous:
            return False
        return self.canEdit(user) or \
            Admin.objects.filter(system=self, user=user).exists()

    @classmethod
    def getAdminSystems(cls, user):
        """ returns a pair (admin, others) of systems for a given user """

        # if a user is a super admin all of them
        if is_superadmin(user):
            return VotingSystem.objects.all()
        if user.is_anonymous:
            return VotingSystem.objects.none()

        return VotingSystem.objects.filter(admin__user=user)

    @classmethod
    def splitSystemsFor(cls, user):
        """ returns a pair (admin, others) of systems for a given user """

        # if a user is a super admin, return (all, none)
        if is_superadmin(user):
            return VotingSystem.objects.all(), VotingSystem.objects.none()

        # if are anonymous return (none, all)
        if user.is_anonymous:
            return VotingSystem.objects.none(), VotingSystem.objects.all()

        # else we need two quieries
        administered = VotingSystem.objects.filter(admin__user=user)
        others = VotingSystem.objects.exclude(admin__user=user)

        # and return both QuerySets
        return administered, others


admin.site.register(VotingSystem)
