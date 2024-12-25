from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, UUIDField
from django.utils.translation import gettext_lazy as _

from ghsystems.apps.core.managers import UserManager


class User(AbstractUser):
    """Custom User Model
    Each User represents a taxpayer of the Tax Authority"""
    id = UUIDField(primary_key=True, editable=False, default=uuid4)
    email = EmailField(_("email address"), unique=True)

    objects = UserManager()
