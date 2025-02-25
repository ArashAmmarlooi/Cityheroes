from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import random


# Custom User Model
class User(AbstractUser):  # Extends Django's built-in User model
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)  # Stores OTP for verification
    is_verified = models.BooleanField(default=False)  # For OTP verification

    # User type: Are they a helper, professional, or both?
    USER_TYPES = [
        ('helper', 'Helper'),
        ('professional', 'Professional'),
        ('both', 'Both')
    ]
    USERNAME_FIELD = 'email'  # User logs in with email instead of username
    REQUIRED_FIELDS = ['phone_number']
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='both')
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))  # 6-digit OTP
        self.save()

# User Profile Model
class UserProfile(models.Model):
    firstname  = models.CharField(max_length=50, blank=True)
    lastname  = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Additional profile details
    profile_picture = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True)
    profession = models.CharField(max_length=100, blank=True)
    experience = models.TextField(blank=True)
    # Skills (Many-to-Many)
    skills = models.ManyToManyField('Skill', blank=True, related_name='users_with_skill')
    # Availability and Contact Preferences
    availability = models.BooleanField(default=True)
    preferred_contact_method = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('phone', 'Phone'), ('messaging', 'Messaging Platform')],
        default='email'
    )
    # User Statistics
    rating = models.FloatField(blank=True, null=True)
    help_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Profile"

# Skills Model
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
