from django.shortcuts import render
from django.views import View

from .models import Blog, PinnedBlog

class IndexView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        pinned_blogs = PinnedBlog.objects.all()[:4]
        context = {
            'blogs':blogs,
            'pinned_blogs':pinned_blogs
        }
        return render(request, 'blog/index.html', context)
    
class BlogDetailView(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        blog.views += 1
        blog.save()
        blogs = Blog.objects.all()[:3]
        context = {
            'blog':blog,
            'blogs':blogs
        }

        return render(request, 'blog/post.html', context)
    
class AuthorView(View):
    def get(self, request):
        return render(request, 'blog/author.html')