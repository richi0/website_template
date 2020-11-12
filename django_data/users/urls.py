from django.urls import path, re_path
from allauth.account import views as auth_views

from .views import SignupPageView

urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='account_logout'),
    path('signup/', auth_views.SignupView.as_view(template_name='users/signup.html'),
         name='account_signup'),

    # Email
    path('email/', auth_views.EmailView.as_view(), name='account_email'),
    re_path(r"^confirm_email/(?P<key>[-:\w]+)/$",
            auth_views.ConfirmEmailView.as_view(
                template_name='users/confirm_email.html'),
            name="account_confirm_email"),

    # Password
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name='users/change_password.html'), name='account_change_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='users/reset_password.html'), name='account_reset_password'),
    re_path(r"^confirm_reset_password/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            auth_views.PasswordResetFromKeyView.as_view(
                template_name='users/reset_password_confirm.html'),
            name="account_reset_password_from_key"),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),
         name="account_reset_password_done"),
    path('reset_password/done/key/', auth_views.PasswordResetFromKeyDoneView.as_view(template_name='users/reset_password_from_key_done.html'),
         name="account_reset_password_from_key_done"),
]
