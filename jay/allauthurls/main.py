from django.conf.urls import url, include
import importlib

from allauth.socialaccount import providers

from allauth import app_settings

urlpatterns = [url('^', include('allauth.account.urls'))]

if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [url('^social/', include('jay.allauthurls.socialaccounts'))]


for provider in providers.registry.get_list():
   try:
       prov_mod = importlib.import_module(provider.get_package() + '.urls')
   except ImportError:
       continue
   prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
   if prov_urlpatterns:
       urlpatterns += prov_urlpatterns
