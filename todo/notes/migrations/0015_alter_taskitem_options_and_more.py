# Generated by Django 4.1 on 2022-08-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_alter_taskitem_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskitem',
            options={'ordering': ['-unfinished']},
        ),
        migrations.RenameField(
            model_name='taskitem',
            old_name='category_task',
            new_name='category',
        ),
    ]
