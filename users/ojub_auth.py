from django.conf import settings

import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

OPENJUB_BASE = "http://localhost:9000/"


def get_all():
    client = BackendApplicationClient(client_id=settings.DREAMJUB_CLIENT_ID)
    dreamjub = OAuth2Session(client=client)
    dreamjub.fetch_token(
        token_url=settings.DREAMJUB_CLIENT_URL + 'login/o/token/',
        client_id=settings.DREAMJUB_CLIENT_ID,
        client_secret=settings.DREAMJUB_CLIENT_SECRET)

    # iterate over the pages (while there is a next)
    results = []
    next = settings.DREAMJUB_CLIENT_URL + 'api/v1/users/'

    while next:
        res = dreamjub.get(next)
        if not res.ok:
            raise Exception(
                'Unable to retrieve current list of students, '
                'please try again later. ')

        res = res.json()
        results += res['results']
        next = res['next'] if 'next' in res else None

    return results
