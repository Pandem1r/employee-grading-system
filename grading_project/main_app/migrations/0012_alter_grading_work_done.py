# Generated by Django 5.0.9 on 2024-09-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_grading_rating_alter_profile_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grading',
            name='work_done',
            field=models.TextField(blank=True, verbose_name='Выполненная работа'),
        ),
    ]