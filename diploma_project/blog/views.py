from django.shortcuts import render, get_object_or_404
from .models import Post

def home_page(request):
    return render(request, 'home.html', context={})

def blog_list(request):
    list_o = Post.objects.all()
    return render(request, 'blog_list.html', {'list': list_o})


def blog_detail(request, post):
    post = get_object_or_404(
        Post, slug=post
        )
    return render(request,'blog_detail.html', {'post': post})

# Create your views here.
