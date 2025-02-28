import random
import string
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta

def generate_code(length=6):
    """Generate a random numeric code of given length"""
    return ''.join(random.choices(string.digits, k=length))

def generate_email_verification_code(user):
    """Generate and store email verification code"""
    code = generate_code()
    cache.set(f'email_verification_{user.email}', code, timeout=600)  # 10 minutes
    return code

def verify_email_code(email, code):
    """Verify the email verification code"""
    cached_code = cache.get(f'email_verification_{email}')
    return cached_code == code

def send_email_verification(email, code):
    """Send verification code to user's email"""
    subject = 'Your Email Verification Code'
    message = f'Use this code to verify your email: {code}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

def send_phone_otp(phone_number):
    """Send OTP to phone number"""
    otp = generate_code()
    cache.set(f'phone_otp_{phone_number}', otp, timeout=300)  # 5 minutes
    # Integrate with SMS gateway here (e.g., Twilio)
    print(f'Sending OTP {otp} to phone number {phone_number}')
    return otp

def verify_phone_otp(phone_number, otp):
    """Verify the phone OTP"""
    cached_otp = cache.get(f'phone_otp_{phone_number}')
    return cached_otp == otp
