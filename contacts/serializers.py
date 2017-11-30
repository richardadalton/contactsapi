from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contact

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name="contacts-detail")

    class Meta:
        model = Contact
        fields = ('url', 'id', 'owner',
                  'first_name', 'last_name', 'email')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(many=True, view_name='contacts-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="users-detail")
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'contacts')


