# Generated by Django 4.1 on 2022-08-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_alter_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='default_categorys',
            field=models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('PERSONAL', 'PERSONAL'), ('SHOPPING', 'SHOPPING'), ('WISHLIST', 'WISHLIST'), ('WORK', 'WORK')], default='DEFAULT', max_length=20),
        ),
    ]