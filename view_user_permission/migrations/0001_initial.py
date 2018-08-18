# Generated by Django 2.1 on 2018-08-18 06:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.CharField(max_length=128)),
                ('action', models.SmallIntegerField(choices=[('retrieve', 'GET'), ('create', 'POST'), ('update', 'PUT'), ('partial_update', 'PATCH'), ('destroy', 'DELETE')])),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(related_name='permissions', to='view_user_permission.Permission'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='consist', to=settings.AUTH_USER_MODEL),
        ),
    ]
