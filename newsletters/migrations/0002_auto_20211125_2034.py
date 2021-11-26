# Generated by Django 3.2.9 on 2021-11-26 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
