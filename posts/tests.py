from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from .serializers import PostSerializer


class PostListTests(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='adam', password='password123')

    def test_can_list_posts(self):
        # Test if the response contains the list of posts
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        print(response.data)
        print(len(response.data))
    
    def test_create_post_authenticated(self):
        # Test if a logged-in user can create a post
        self.client.login(username='adam', password='password123')
        data = {'title': 'a title'}
        response = self.client.post('/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
    
    def test_create_post_unauthenticated(self):
        # Test if an unauthenticated user receives a 403 (FORBIDDEN) response
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
