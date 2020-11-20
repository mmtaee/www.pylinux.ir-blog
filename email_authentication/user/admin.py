from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'superuser')
    list_filter = ('superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('superuser', 'staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# حذف فیلد گروه
from django.contrib.auth.models import Group
admin.site.unregister(Group)