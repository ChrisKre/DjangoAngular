from rest_framework import serializers
from registers.models import Register
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    questionRegisterOwners = serializers.PrimaryKeyRelatedField(many=True, queryset=Register.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'questionRegisterOwners']


class RegisterSerializer(serializers.ModelSerializer):

    owner = UserSerializer(many=True)

    class Meta:
        model = Register
        fields = ['id', 'name', 'owner', 'type', 'timestamp', 'updated']
