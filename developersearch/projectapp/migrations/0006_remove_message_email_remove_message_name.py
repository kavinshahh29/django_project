# Generated by Django 5.0.1 on 2024-02-23 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_message_reciever_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
    ]
