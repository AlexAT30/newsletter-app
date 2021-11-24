# Generated by Django 3.2.9 on 2021-11-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='dummy text', max_length=100)),
                ('description', models.CharField(default='dummy description', max_length=400)),
                ('img', models.CharField(default='image_dummmy_url', max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('tags', models.ManyToManyField(related_name='tags', to='tags.Tag')),
            ],
        ),
    ]
