# Generated by Django 5.0.1 on 2024-02-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0006_remove_message_email_remove_message_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]