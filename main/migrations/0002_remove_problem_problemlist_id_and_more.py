# Generated by Django 4.0.4 on 2022-05-22 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='problemList_id',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='problem_number',
        ),
        migrations.DeleteModel(
            name='ProblemList',
        ),
    ]