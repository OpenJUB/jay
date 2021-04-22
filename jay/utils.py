from django.core.exceptions import PermissionDenied


def memoize(f):
    memo = {}

    def helper(*x):
        key = str(x)
        if key not in memo:
            memo[key] = f(*x)
        return memo[key]

    return helper


def is_superadmin(user):
    """ Checks if a user is a superadmin. """
    return user.is_superuser


def is_elevated(user):
    """ Checks if a user is an admin for some voting system """
    if not user.is_superuser:
        if not user.admin_set.count() > 0:
            return False
    return True


def superadmin(handler):
    """ Requires a user to be a superadmin. """

    def helper(request, *args, **kwargs):
        if not is_superadmin(request.user):
            raise PermissionDenied
        return handler(request, *args, **kwargs)

    return helper


def elevated(handler):
    """ Requires a user to be elevated user """

    def helper(request, *args, **kwargs):
        if not is_elevated(request.user):
            raise PermissionDenied

        return handler(request, *args, **kwargs)

    return helper


def get_user_details(user):
    """ Gets a dict() object representing user data """

    try:
        data = user.socialaccount_set.get(provider="google").extra_data
        return data
    except:
        # fallback to an in-active user with just a username flag
        return {'username': user.username, 'active': False}
