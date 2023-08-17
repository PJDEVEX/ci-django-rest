from rest_framework import serializers
from .models import Post
from likes.models import Like

# Serializer for the Post model


class PostSerializer(serializers.ModelSerializer):
    # Read-only field showing the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')
    # Serializer method field to determine if the current user is the owner of the post
    is_owner = serializers.SerializerMethodField()
    # Read-only field showing the profile ID of the owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    # Read-only field showing the profile image URL of the owner
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # Define the like id feild
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validate the uploaded image size, width, and height.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
            """
            Method to determine if the current user is the owner of the post.
            """
            request = self.context['request']
            return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
                ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
        ]

