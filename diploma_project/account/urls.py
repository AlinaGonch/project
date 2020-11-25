from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('personal_page/', views.personal_page, name='personal_page'),
    path('register/', views.reg_page, name='reg_page'),
    path('login/', views.log_page, name='log_page'),
    path('logout/', views.logout_user, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset_password/done', auth_views.PasswordResetDoneView.as_view(template_name='password_sent.html'), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_form.html'), name='password_reset_confirm'),
    path('reset_password/complete', auth_views.PasswordResetCompleteView.as_view(template_name='changed_password_mess.html'), name='password_reset_complete'),
]