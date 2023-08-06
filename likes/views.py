from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from drf.permissions import IsOwnerOrReadOnly

class LikeList(generics.ListCreateAPIView):
    """
    List all likes and create new likes.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Set the owner of the like as the user making the request.
        """
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and delete a like by ID.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
