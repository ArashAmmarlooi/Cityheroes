from django.contrib import admin

# Register your models here.
from accounts.models import User, UserProfile, Skill


# Register User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('id', 'username', 'email')  # Display fields in admin list
  search_fields = ('username', 'email')  # Add search functionality
  list_filter = ('username', )  # Add filter options


# Register UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'profession', 'availability', 'rating', 'help_count')
  search_fields = ('user__username', 'profession')
  list_filter = ('availability', 'rating')


# Register Skill model
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description')
  search_fields = ('name', )
