# Generated by Django 2.1 on 2018-08-18 08:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_user_permission', '0003_auto_20180818_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='id',
        ),
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.IntegerField(default=0, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(related_name='groups', to='view_user_permission.Permission'),
        ),
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='permission',
            name='action',
            field=models.CharField(choices=[('retrieve', 'retrieve'), ('list', 'list'), ('create', 'create'), ('update', 'update'), ('partial_update', 'partial_update'), ('destroy', 'destroy')], max_length=16),
        ),
    ]