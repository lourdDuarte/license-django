from django.contrib import admin
from profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin (admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'created',
    ]

    fieldsets = (
            ('Perfil', {
                'fields':(
                    ('user'),
                ),
            }),

            ('Date', {
                'fields':(
                    ('created', 'modified'),
                ),
            }),
        )
    
    readonly_fields = ('created', 'modified')


class ProfileInLine (admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseAdmin):

    inlines = (ProfileInLine,)
    list_display = (
        'id',
        'username', 
        'email', 
        'first_name', 
        'last_name',
        'is_staff',
        'is_active',)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)