# Generated by Django 3.2.9 on 2021-11-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
