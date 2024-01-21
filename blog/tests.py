"""
Modified by:
HD
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@mail.com',
            password='123'
        )

        self.post = Post.objects.create(
            title='some title idk',
            body='Lorem ipsum',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'some title idk')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Lorem ipsum')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lorem ipsum')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'some title idk')
        self.assertTemplateUsed(response, 'post_detail.html')