from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import mixins
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        # list comes from mixins.ListModelMixin
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # create comes from mixins.CreateModelMixin
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        # retrieve comes from mixins.RetrieveModelMixin
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # update comes from  mixins.UpdateModelMixin
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # delete comes from mixins.DestroyModelMixin
        return self.destroy(request, *args, **kwargs)