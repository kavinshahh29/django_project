# Generated by Django 5.0.1 on 2024-03-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_profile_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='About',
            field=models.CharField(blank=True, default=' ', max_length=500, null=True),
        ),
    ]
