from django.contrib import admin

# Register your@
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'password', 'id']
