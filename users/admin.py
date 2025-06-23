from django.contrib import admin

from .models import User, Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ("id", "invited_by", "invited_user", "status", "created_at")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username", "created_at")
    list_filter = ("created_at",)
    search_fields = ("id", "first_name", "last_name", "username")
