from django.contrib.admin import (
    AdminSite,
    register as admin_register
)
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _


UserModel = get_user_model()


class AdmininstrationSite(AdminSite):
    AdminSite.site_header = 'GH Systems ADMIN'
    AdminSite.site_title = AdminSite.site_header


@admin_register(UserModel)
class UserAdmin(DjangoUserAdmin):
    """Custom User Admin for Admin Site"""
