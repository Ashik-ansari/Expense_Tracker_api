# Generated by Django 4.0.5 on 2022-06-27 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_expense_user_expensecategory_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='Price',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
