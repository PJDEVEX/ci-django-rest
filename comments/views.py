# Step 1: Import necessary modules
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from drf.permissions import IsOwnerOrReadOnly


# Step 2: Define CommentList view
class CommentList(generics.ListCreateAPIView):
    # Step 3: Set serializer class and permission classes
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Step 4: Define queryset to list all comments
    queryset = Comment.objects.all()

    # Step 5: Implement perform_create to set user as the owner of the comment
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Step 6: Define CommentDetail view
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # Step 7: Set serializer class to CommentDetailSerializer
    serializer_class = CommentDetailSerializer

    # Step 8: Set permission_classes to IsOwnerOrReadOnly
    permission_classes = [IsOwnerOrReadOnly]

    # Step 9: define queryset
    queryset = Comment.objects.all()
