# Generated by Django 4.0.3 on 2022-03-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_alter_youtuber_camera_type_alter_youtuber_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
