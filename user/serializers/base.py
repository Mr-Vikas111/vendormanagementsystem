from rest_framework import serializers 
from user.models import base as  base_user_models

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = base_user_models.User
        fields = ['email','password']