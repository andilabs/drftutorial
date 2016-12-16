from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from tutorial.quickstart import views

admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include('snippets.urls')),
]
