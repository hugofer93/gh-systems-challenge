# Generated by Django 4.2.17 on 2024-12-21 18:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('available', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=80)),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('COMPLETED', 'completed')], default='PENDING', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
