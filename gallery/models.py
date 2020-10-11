from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = [
  ('PERSONAL', 'Personal'), 
  ('PROFESSIONAL', 'Professional'), 
  ('BUSINESS', 'Business'), 
  ('RELIGIOUS', 'Religious'),
  ('POLITICS','Politics'),
]
  

class Post(models.Model):
  image = models.ImageField()
  title = models.CharField(max_length=30, default='Farming')
  category = models.CharField(max_length=13, choices=CATEGORY_CHOICES, default='Personal')
  descritption = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.descritption[:50]

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  text = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.text[:50]
