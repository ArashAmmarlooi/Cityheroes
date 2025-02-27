from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    RegisterUserSerializer,
    VerifyEmailSerializer,
    LoginSerializer,
    PhoneLoginSerializer,
    VerifyOTPSerializer
)

User = get_user_model()


class RegisterUserView(generics.GenericAPIView):
    """API endpoint for user registration (email & password)"""
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        """Handle user registration and send email verification code"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successful! Please verify your email."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(generics.GenericAPIView):
    """API endpoint for verifying email"""
    serializer_class = VerifyEmailSerializer

    def post(self, request, *args, **kwargs):
        """Verify the email and return a JWT token"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Email verified successfully!",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """API endpoint for user login (email/password)"""
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """Authenticate the user and return a JWT token"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Login successful!",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneLoginView(generics.GenericAPIView):
    """API endpoint for phone number login (request OTP)"""
    serializer_class = PhoneLoginSerializer

    def post(self, request, *args, **kwargs):
        """Send OTP to the provided phone number"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "OTP has been sent to your phone number."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(generics.GenericAPIView):
    """API endpoint for verifying OTP"""
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        """Verify OTP and return a JWT token"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "OTP verified successfully!",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
