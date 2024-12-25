from uuid import uuid4

from django.db.models import BooleanField, DateTimeField, Model, UUIDField

from ghsystems.apps.utils.managers import BaseManager


class BaseModel(Model):
    """Base Model for project."""
    available = BooleanField(default=True)
    creation_date = DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True


class BaseUUIDModel(BaseModel):
    """Base UUID Model for project."""
    id = UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True
