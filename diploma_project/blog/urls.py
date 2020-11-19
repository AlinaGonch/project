from django.urls import path
from blog.views import blog_list, blog_detail

urlpatterns =[
    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug:slug>', blog_detail, name='blog_detail'),
]