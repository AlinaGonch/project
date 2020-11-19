from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_list(request):
    list = Post.objects.all()
    return render(request, 'blog_list.html', {'list': list})


def blog_detail(request, year, month, day, post):
    post = get_list_or_404(
        Post, slug=post,
        status='publsihed',
        publish_year=year,
        publish_month=month,
        publish_day=day,
        )
    return render(request,'blog_detail.html', {'post': post})

# Create your views here.
