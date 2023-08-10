from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment, Post

# Serializer for the Comment model
class CommentSerializer(serializers.ModelSerializer):
    # Read-only field showing the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')
    # Serializer method field to determine if the current user is the owner of the post
    is_owner = serializers.SerializerMethodField()
    # Read-only field showing the profile ID of the owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    # Read-only field showing the profile image URL of the owner
    profile_image = serializers.ReadOnlyField(source='owner.profile.image_url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Method to determine if the current user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        """
        Get a human-readable representation of the 'created_at' field
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Get a human-readable representation of the 'updated_at' field
        """
        return naturaltime(obj.created_at)

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'is_owner', 'profile_id',
        'profile_image', 'post', 'created_at', 'updated_at',
        'content'
        ]

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for representing a detailed view of a comment.

    Inherits from CommentSerializer and adds an additional field:
    - post: Represents the associated post's ID (read-only).

    The post field is a read-only field, which means it can only be used
    for serialization and will not be used for deserialization when creating
    or updating a comment. It shows the ID of the post to which the comment
    belongs.
    """
    post = serializers.ReadOnlyField(source='Post.id')
