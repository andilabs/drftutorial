from rest_framework import serializers

from django.contrib.auth.models import User

from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    # The untyped ReadOnlyField is always read-only, and will be used for serialized representations,
    # but will not be used for updating model instances when they are deserialized.
    # We could have also used CharField(read_only=True) here.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
