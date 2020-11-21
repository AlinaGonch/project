from django.urls import path
from .views import log_page, reg_page, logout_user

urlpatterns = [
    path('register/', reg_page, name='reg_page'),
    path('login/', log_page, name='log_page'),
    path('logout/', logout_user, name='logout')
]