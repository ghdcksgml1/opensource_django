# Generated by Django 4.0.4 on 2022-05-22 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_problem_problemlist_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='created_date',
        ),
    ]
