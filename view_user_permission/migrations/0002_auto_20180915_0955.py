# Generated by Django 2.0.4 on 2018-09-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_user_permission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]