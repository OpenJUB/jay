from django import template
from settings.models import VotingSystem
from jay import utils

register = template.Library()


@register.filter()
def getAdminSystems(user):
    return VotingSystem.getAdminSystems(user)


@register.filter()
def canEdit(user, system):
    print('checking', system, user)
    return system.canEdit(user)


@register.filter()
def isSuperAdmin(user):
    return utils.is_superadmin(user)
