from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(User, UserAdmin)
