# Generated by Django 4.1 on 2022-08-19 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_note_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2022, 8, 19, 17, 36, 44, 484450, tzinfo=datetime.timezone.utc))),
                ('unfinished', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('PERSONAL', 'PERSONAL'), ('SHOPPING', 'SHOPPING'), ('WISHLIST', 'WISHLIST'), ('WORK', 'WORK')], default='DEFAULT', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='NotesList',
        ),
    ]