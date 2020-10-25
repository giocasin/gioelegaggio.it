from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.views import generic
from .models import Post

class Index(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class LastPost(generic.ListView):
    queryset = Post.objects.latest('created_on')
    template_name = 'blog/last_post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'