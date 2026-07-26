from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # Which model to use.
        fields = ["username","email","password"]
        extra_kwargs ={
            'password':{'write_only':True}  # it not include the password.
        }

    def create(self,validated_data):
        user = User.objects.create_user(   # hashes the password, Saves user securely. 
            username = validated_data['username'],
            email =  validated_data['email'],
            password = validated_data['password']
        )
        return user

class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["owner", "created_at", "updated_at"]
