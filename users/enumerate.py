from django.conf import settings


from google.oauth2 import service_account
import googleapiclient.discovery


from typing import List, Optional, Dict, Any
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import Resource


def make_delegated_credentials(scopes: List[str]) -> Credentials:
    """ Creates a delegated_credentials object """
    credentials = service_account.Credentials.from_service_account_file(
        settings.GSUITE_AUTH_FILE, scopes=scopes)
    delegated_credentials = credentials.with_subject(
        settings.GSUITE_ADMIN_USER)
    return delegated_credentials


def make_directory_service() -> Resource:
    """ Makes a Google API directory service """

    delegated_credentials = make_delegated_credentials(
        ['https://www.googleapis.com/auth/admin.directory.user'])
    return googleapiclient.discovery.build('admin', 'directory_v1', credentials=delegated_credentials)


def get_all():
    service = make_directory_service()

    users = service.users()
    request = users.list(domain='jacobs-alumni.de', projection='basic', maxResults=500)


    out = []

    while request is not None:
        users_doc = request.execute()

        out.extend(users_doc["users"])

        request = users.list_next(request, users_doc)


    return out

def get_one(userKey):
    service = make_directory_service()

    users = service.users()
    request = users.get(projection='basic', userKey=userKey)

    user = request.execute()


    return user