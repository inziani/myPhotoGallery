from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from gallery.models import Post, Comment

# Create your views here

class PostList(ListView):
  model = Post
  template_name = 'home.html'
  context_object_name = 'all_posts_lists'

class PostCreate(CreateView):
  model = Post
  template_name = 'new_post.html'
  fields = ['image', 'descritption', 'author']
  success_url = '/'

class CommentForm(forms.Form):
  comment = forms.CharField()

class PostDetail(DetailView):
  model = Post
  template_name = 'post_detail.html'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['comment_form'] = CommentForm()
    return context

  def post(self, request, *args, **kwargs):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = Comment(author = request.user, post = self.get_object(), text = comment_form.cleaned_data['comment'])
      comment.save()
    else:
      raise Exception
    return redirect(reverse('comments', args=[self.get_object().id]))




