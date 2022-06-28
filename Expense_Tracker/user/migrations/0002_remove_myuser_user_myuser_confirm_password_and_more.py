# Generated by Django 4.0.5 on 2022-06-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user',
        ),
        migrations.AddField(
            model_name='myuser',
            name='confirm_password',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='fullname',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='mobile_number',
            field=models.CharField(default=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=False, max_length=255),
        ),
    ]