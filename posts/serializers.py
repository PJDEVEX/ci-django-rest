from rest_framework import serializers
from .models import Post

# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    # Read-only field showing the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')
    # Serializer method field to determine if the current user is the owner of the post
    is_owner = serializers.SerializerMethodField()
    # Read-only field showing the profile ID of the owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    # Read-only field showing the profile image URL of the owner
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image_url')

    def get_is_owner(self, obj):
        """
        Method to determine if the current user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image', 'is_owner']
