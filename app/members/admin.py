from django.contrib import admin

from members.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'send_email', 'authorization')