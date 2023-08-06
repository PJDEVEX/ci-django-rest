from rest_framework import serializers
from .models import Like

# Serializer for the Comment model
class LikeSerializer(serializers.ModelSerializer):
    # Read-only field showing the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields =  ['id', 'created_at', 'owner', 'post']
