from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView #추가
from django.core.urlresolvers import reverse_lazy #추가
from blog.models import Post

# Create your views here.
class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post

#=============================아래 추가
class PostCV(CreateView):
    model = Post
    fields = ['title','image','description']
    success_url = reverse_lazy('blog_index')

class PostUV(UpdateView):
    model = Post
    fields = ['title', 'image', 'description']
    success_url = reverse_lazy('blog_index')

class PostRV(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_index')





    