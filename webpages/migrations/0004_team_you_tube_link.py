# Generated by Django 4.0.3 on 2022-03-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='you_tube_link',
            field=models.URLField(default=True, max_length=1000),
        ),
    ]
