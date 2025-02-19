from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
  id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(unique=True)
  password_hash = models.CharField(max_length=128)
  # UserProfile will reference this table with a foreign key


class UserProfile(models.Model):
  user = models.OneToOneField(User,
                              on_delete=models.CASCADE,
                              related_name='profile')
  first_name = models.CharField(max_length=50, blank=True)
  last_name = models.CharField(max_length=50, blank=True)
  profile_picture = models.URLField(blank=True, null=True)
  bio = models.TextField(blank=True)

  profession = models.CharField(max_length=100, blank=True)
  experience = models.TextField(blank=True)
  skills = models.ManyToManyField('Skill',
                                  blank=True,
                                  related_name='users_with_skill')

  availability = models.BooleanField(default=True)
  preferred_contact_method = models.CharField(max_length=50,
                                              choices=[('email', 'Email'),
                                                       ('phone', 'Phone'),
                                                       ('messaging',
                                                        'Messaging Platform')],
                                              default='email')

  rating = models.FloatField(blank=True, null=True)
  help_count = models.PositiveIntegerField(default=0)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True)
