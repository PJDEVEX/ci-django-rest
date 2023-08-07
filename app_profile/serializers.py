from rest_framework import serializers
from .models import Profile
from followers.models import Follower

# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    # SerializerMethodField to add an extra field 'is_owner'
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()  # Define the following_id field
    # New fields for post count, followers count, and following count
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        # Method to determine if the current user is the owner of the profile
        request =self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None


    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
        'content', 'image', 'is_owner', 'following_id',
        'posts_count', 'followers_count', 'following_count',
        ]
    
    

