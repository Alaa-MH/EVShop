from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email','password1', 'password2', ),
        }),
     )

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if 'default-user.png' not in object.profile_picture.url :
           return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
        else:
            return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.get_default_profile_picture))

    thumbnail.short_description = 'profile_picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
