from rest_framework import serializers
from .models import User

# Serializer pour le user Model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'city']
