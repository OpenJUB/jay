from django.db import models
from django.contrib.auth.models import User

from django.contrib import admin


# Create your models here.
class Admin(models.Model):
    user = models.ForeignKey(User)
    system = models.ForeignKey("settings.VotingSystem")

    class Meta():
        unique_together = (("system", "user"))

    def __str__(self):
        return u'[%s] %s' % (self.system.machine_name, self.user)


admin.site.register(Admin)
