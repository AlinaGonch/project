from django.urls import path
from blog.views import (blog_list, blog_detail, home_page)

urlpatterns =[
    path('home/', home_page, name='home_blog'),
    path('blog', blog_list, name='blog_list'),
    path('blog/<slug:post>', blog_detail, name='blog_detail'),
]