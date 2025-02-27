from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from .utils import (
    generate_email_verification_code,
    verify_email_code,
    send_email_verification,
    send_phone_otp,
    verify_phone_otp
)
from rest_framework.validators import UniqueValidator

User = get_user_model()


from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirmation = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=True)  # Add username field

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confirmation')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],  # Pass username
            password=validated_data['password'],
            is_active=False  # User is inactive until email verification
        )
        code = generate_email_verification_code(user)
        send_email_verification(user.email, code)
        return user



class VerifyEmailSerializer(serializers.Serializer):
    """Serializer for email verification"""
    email = serializers.EmailField()
    verification_code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('verification_code')
        if not verify_email_code(email, code):
            raise serializers.ValidationError("Invalid or expired verification code.")
        return attrs

    def save(self, **kwargs):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login via email and password"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    verification_code = serializers.CharField(max_length=6, write_only=True, required=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        verification_code = attrs.get('verification_code')

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid login credentials.")

        # Check if email is verified
        if not user.is_active:
            # If verification code is provided, attempt to verify
            if verification_code:
                if not verify_email_code(email, verification_code):
                    raise serializers.ValidationError("Invalid or expired verification code.")
                user.is_active = True
                user.save()
            else:
                # Send verification code
                code = generate_email_verification_code(user)
                send_email_verification(user.email, code)
                raise serializers.ValidationError("Email not verified. Verification code sent to your email.")
        attrs['user'] = user
        return attrs


class PhoneLoginSerializer(serializers.Serializer):
    """Serializer for phone number login"""
    phone_number = serializers.CharField(max_length=15)

    def validate_phone_number(self, value):
        # Add phone number validation logic here (e.g., regex)
        return value

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        user, created = User.objects.get_or_create(phone_number=phone_number)
        # Send OTP to the phone number
        otp = send_phone_otp(phone_number)
        return {'phone_number': phone_number}


class VerifyOTPSerializer(serializers.Serializer):
    """Serializer for OTP verification"""
    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        otp = attrs.get('otp')
        if not verify_phone_otp(phone_number, otp):
            raise serializers.ValidationError("Invalid or expired OTP.")
        return attrs

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        user, _ = User.objects.get_or_create(phone_number=phone_number)
        return user
