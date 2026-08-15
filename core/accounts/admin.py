from django.contrib import admin
from .models import User , Profile
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = ("email", "is_staff", "is_active", "created_time")
    search_fields = ("email",)
    ordering = ("email",)
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),

        ("info", {"fields": ("is_staff", "is_active" , "is_superuser")}),
        ("groups", {"fields": ("groups","user_permissions")}),
        
    )
    add_fieldsets = (
        (
            "MIO",
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2" , "is_staff" , "is_active" , "is_superuser"),
            },
        ),
    )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "image", "description")
    


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
