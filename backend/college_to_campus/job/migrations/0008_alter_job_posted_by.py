# Generated by Django 5.0.7 on 2024-08-06 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_company_logo'),
        ('user', '0009_studentuser_employeeuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='posted_by',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='user.employeeuser'),
        ),
    ]
