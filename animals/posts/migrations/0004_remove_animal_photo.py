# Generated by Django 3.2 on 2023-03-21 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_color_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='photo',
        ),
    ]
