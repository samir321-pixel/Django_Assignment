from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models


class CoreRegisterSerializer(RegisterSerializer):

    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'first_name')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'password1': self.validated_data.get('password1', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data.get('first_name')
        user.Date_of_Birth = self.cleaned_data.get('Date_of_Birth')
        user.save()
        adapter.save_user(request, user, self)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'first_name')


class ChangePasswordSerializer(serializers.Serializer):
    model = models.User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data

        return {serializer_data}
