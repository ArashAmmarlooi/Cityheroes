from django.urls import path
from .views import (
    RegisterUserView,
    VerifyEmailView,
    LoginView,
    PhoneLoginView,
    VerifyOTPView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('phone-login/', PhoneLoginView.as_view(), name='phone_login'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
]
