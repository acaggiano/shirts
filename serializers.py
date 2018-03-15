from django.contrib.auth.models import User, Group
from .models import Shirt
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ShirtSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='shirts-detail')

    class Meta:
        model = Shirt
        fields = ('url', 'id', 'name', 'worn', 'image')
