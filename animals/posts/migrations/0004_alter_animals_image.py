# Generated by Django 3.2 on 2023-03-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_animals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
