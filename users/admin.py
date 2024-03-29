from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "slackUsername",
        "backend",
        "age",
        "bio",
    )


admin.site.register(User, UserAdmin)
