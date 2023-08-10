from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def root_route(request):
    """
    Handles the root route of the API.

    `@api_view` decorator, specifies that it only accepts HTTP GET requests. 
    When a GET request is made to the root route.
    Returns a JSON response containing a welcome message.
    """
    return Response({'message': 'Welcome to our API!'})
