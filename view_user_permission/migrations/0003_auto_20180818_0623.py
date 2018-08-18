# Generated by Django 2.1 on 2018-08-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_user_permission', '0002_auto_20180818_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='NO_NAME', max_length=64),
        ),
        migrations.AlterField(
            model_name='permission',
            name='action',
            field=models.CharField(choices=[('GET', 'retrieve'), ('POST', 'create'), ('PUT', 'update'), ('PATCH', 'partial update'), ('DELETE', 'destroy')], max_length=16),
        ),
    ]