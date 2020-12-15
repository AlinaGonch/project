from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('personal_page/', views.personal_page, name='personal_page'),
    path('register/', views.reg_page, name='reg_page'),
    path('login/', views.log_page, name='log_page'),
    path('logout/', views.logout_user, name='logout'),

    path('reset_password/', views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done', views.password_success, name='password_reset_done'),
    path('reset_password/<uidb64>/<token>', views.PasswordSetView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete', views.changed_password_message, name='password_reset_complete'),
]