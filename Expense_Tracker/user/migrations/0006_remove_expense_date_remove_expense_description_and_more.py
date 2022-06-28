# Generated by Django 4.0.5 on 2022-06-27 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_expense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='description',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.AddField(
            model_name='expense',
            name='Date',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='expense',
            name='Description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='expensecategory',
            name='CategoryName',
            field=models.CharField(max_length=500, null=True),
        ),
    ]