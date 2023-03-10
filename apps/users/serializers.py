from rest_framework import serializers

from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255, write_only = True
    )        
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age', 'password', 'password2')