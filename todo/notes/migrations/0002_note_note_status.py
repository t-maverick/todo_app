# Generated by Django 4.1 on 2022-08-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_status',
            field=models.BooleanField(default=True),
        ),
    ]