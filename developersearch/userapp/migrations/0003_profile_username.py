# Generated by Django 5.0.1 on 2024-03-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_rename_email_profile_email_rename_name_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]