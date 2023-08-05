from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from rest_framework import status
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        """
        List all posts.
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new post.
        """
        serializer = PostSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
