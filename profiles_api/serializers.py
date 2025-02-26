from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serialize a name field to test our APIView"""

    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField()


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            # If the field exists, we will "pop" (which means assign the value and remove from the dictionary)
            # the password from the validated data and set it using set_password() (which saves the password as a hash).
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)