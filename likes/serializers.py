from django.db import IntegrityError 
from rest_framework import serializers
from .models import Like

# Serializer for the Comment model
class LikeSerializer(serializers.ModelSerializer):
    # Read-only field showing the username of the owner
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields =  ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            # Try to create a new Like object with the validated data
            return super().create(validated_data)
        except IntegrityError:
            # If an IntegrityError occurs (likely due to a duplicate like),
            # raise a serializers.ValidationError with a custom detail message.
            raise serializers.ValidationError({
                'detail': 'You have already liked this post.'
            })
