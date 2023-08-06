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

    def get_is_owner(self, obj):
        """
        Method to determine if the current user is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

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