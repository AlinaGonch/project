from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_countries, name='countries'),
    path('<int:id>/', views.country_details, name='country_details'),
]
