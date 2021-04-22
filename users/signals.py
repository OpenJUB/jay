from django.dispatch import receiver
from allauth.socialaccount import signals

from . import enumerate

# Load all the details from the user directory for filtering later
@receiver(signals.pre_social_login)
def update_extra_data(request, sociallogin, **kwargs):
    if sociallogin.account.provider != 'google':
        return

    id = sociallogin.account.extra_data['id']
    extra_user = enumerate.get_one(id)

    sociallogin.account.extra_data.update(extra_user)

    # If the social account already exists, save the model again
    if sociallogin.account.pk:
        sociallogin.account.save()

