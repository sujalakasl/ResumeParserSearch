# Generated by Django 4.1.6 on 2023-02-06 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0012_resume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
    ]
