from django.db.models import CharField

from ghsystems.apps.utils.models import BaseUUIDModel


class Tasks(BaseUUIDModel):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'

    STATUS_CHOICES = (
        (PENDING, 'pending'),
        (COMPLETED, 'completed'),
    )

    title = CharField(max_length=30)
    description = CharField(max_length=80)
    status = CharField(max_length=20, default=PENDING, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.title} | {self.status}'
