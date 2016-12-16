from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from snippets.views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)
schema_view = get_schema_view(title='Pastebin API')

# READING on SCHEMA:
# http://www.django-rest-framework.org/api-guide/schemas/
# http://www.coreapi.org/specification/encoding/#core-json-encoding
# https://www.openapis.org/

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
