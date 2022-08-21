# Generated by Django 4.1 on 2022-08-20 10:43

from django.db import migrations, models
import notes.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_rename_category_taskitem_category_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=10, validators=[notes.models.Category.choice_or_make]),
        ),
    ]
