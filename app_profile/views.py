from django.http import Http404
# import status to check the statatus check
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """
    API view to list all profiles.
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles,
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)


class ProfileDetail(APIView):
    # Add the profile details to the view
    serializer_class = ProfileSerializer
    # Allowable permission class
    permission_classes = [IsOwnerOrReadOnly]
    # get_object method to fetch profile by primary key
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            # Checking the permission explicitly
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    # 3. Implement get method to retrieve a profile by id
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    # Implement put method to update a profile by id
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
