from rest_framework import serializers
from users.models import user

class UserSerializer(serializers.ModelSerializer):
    # Serializer for Question models
    class Meta:
        model = user
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
