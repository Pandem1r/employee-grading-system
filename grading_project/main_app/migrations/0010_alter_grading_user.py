# Generated by Django 5.0.8 on 2024-09-07 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_inspectors_audited_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grading',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile', verbose_name='Юзер'),
        ),
    ]
