# Generated by Django 3.2.9 on 2021-11-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20211125_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='img',
            new_name='image_url',
        ),
    ]