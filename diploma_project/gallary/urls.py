from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallary_page, name='gallery')
]