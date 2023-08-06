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

# Create a new class for the PostDetail view tests
class PostDetailTests(APITestCase):
    def setUp(self):
        # Create users for testing
        self.user_adam = User.objects.create_user(username='adam', password='password123')
        self.user_brian = User.objects.create_user(username='brian', password='password123')

        # Create posts for each user
        self.post_adam = Post.objects.create(owner=self.user_adam, title='Adam\'s Post', content='adams content')
        self.post_brian = Post.objects.create(owner=self.user_brian, title='Brian\'s Post', content='Brians content')

    def test_retrieve_post_valid_id(self):
        # Test retrieving a post with a valid ID
        response = self.client.get(f'/posts/{self.post_adam.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.post_adam.id)
        

    def test_retrieve_post_invalid_id(self):
        # Test retrieving a post with an invalid ID
        response = self.client.get('/posts/999/')  # Using an invalid ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='password123')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_another_users_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    

    