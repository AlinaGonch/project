from django.urls import path
from .views import log_page, reg_page, logout_user, personal_page

urlpatterns = [
    path('personal_page/', personal_page, name='personal_page')
    path('register/', reg_page, name='reg_page'),
    path('login/', log_page, name='log_page'),
    path('logout/', logout_user, name='logout')
]