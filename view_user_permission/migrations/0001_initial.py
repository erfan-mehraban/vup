# Generated by Django 2.1 on 2018-08-18 10:25

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
                ('name', models.CharField(default='NO_NAME', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('name', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('view', models.CharField(max_length=128)),
                ('action', models.CharField(choices=[('retrieve', 'retrieve'), ('list', 'list'), ('create', 'create'), ('update', 'update'), ('partial_update', 'partial_update'), ('destroy', 'destroy')], max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(related_name='groups', to='view_user_permission.Permission'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
    ]
