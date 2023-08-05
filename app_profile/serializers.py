from rest_framework import serializers
from .models import Profile

# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    # SerializerMethodField to add an extra field 'is_owner'
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        # Method to determine if the current user is the owner of the profile
        request =self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name',
        'content', 'image', 'is_owner' ]
