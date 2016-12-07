from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from tutorial.quickstart import views

admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
