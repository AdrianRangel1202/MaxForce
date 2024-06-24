from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        

    def to_representation(self, instance):
        return {
            'username': instance.username,
            'email': instance.email,
            'name': instance.name,
            'last_name':instance.last_name
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(instance.password)
        updated_user.save()
        return updated_user
