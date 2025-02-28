# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User, UserProfile, Skill

# # Unregister default User model before registering custom one
# if User in admin.site._registry:
#     admin.site.unregister(User)

# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ('id', 'username', 'email', 'phone_number', 'user_type', 'is_staff', 'is_active')
#     search_fields = ('username', 'email')

#     # Modify fieldsets (Exclude 'email' if it's already in UserAdmin)
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important Dates', {'fields': ('last_login', 'date_joined')}),
#         ('Additional Info', {'fields': ('phone_number', 'user_type')}),  # No duplicate 'email'
#     )

#     # Modify add_fieldsets (for creating new users)
#     add_fieldsets = (
#         (None, {'fields': ('username', 'email', 'password1', 'password2')}),
#         ('Additional Info', {'fields': ('phone_number', 'user_type')}),
#     )

# # ✅ Register User Model Correctly
# admin.site.register(User, CustomUserAdmin)

# # ✅ Register User Profile Model
# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'profession', 'availability')
#     search_fields = ('user__username', 'profession')
#     list_filter = ('availability',)
#     filter_horizontal = ('skills',)

# # ✅ Register Skill Model
# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)
