from rest_framework import serializers

from django.contrib.auth.models import User

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # The untyped ReadOnlyField is always read-only, and will be used for serialized representations,
    # but will not be used for updating model instances when they are deserialized.
    # We could have also used CharField(read_only=True) here.
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')