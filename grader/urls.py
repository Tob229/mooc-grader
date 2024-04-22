import os

from django.conf import settings
from django.urls import include, path, re_path


urlpatterns = [
    re_path(r'^', include('django_prometheus.urls')),
]

import access.urls
urlpatterns.append(path('', include(access.urls)))

if settings.DEBUG:
    import staticfileserver.urls
    urlpatterns.append(path('', include(staticfileserver.urls)))

os.umask(0o002)
