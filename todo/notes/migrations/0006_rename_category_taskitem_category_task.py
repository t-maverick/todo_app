# Generated by Django 4.1 on 2022-08-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_category_category_alter_taskitem_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskitem',
            old_name='category',
            new_name='category_task',
        ),
    ]
