from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from .models import Post

class PostModelTest(TestCase):

  def setUp(self):
    self.user = User.objects.create_superuser('robai', 'robai@gmail.com','test') 
    Post.objects.create(image='val.png', title='Missy', category='Religious', descritption='Migration Test', author=self.user)

  def test_post_creation(self):
    post = Post.objects.get(id=1)
    expected_object_title = f'{post.title}'
    self.assertEqual(expected_object_title, 'Missy')

  def test_view_url_exists_at_proper_location(self): 
    resp = self.client.get('/') 
    self.assertEqual(resp.status_code, 200)

  def test_view_uses_correct_template(self): 
    resp = self.client.get(reverse('home')) 
    self.assertEqual(resp.status_code, 200) 
    self.assertTemplateUsed(resp, 'home.html')
  
