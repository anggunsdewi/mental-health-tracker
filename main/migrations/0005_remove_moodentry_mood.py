# Generated by Django 5.1.1 on 2024-10-02 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_moodentry_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='mood',
        ),
    ]
