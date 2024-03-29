# Generated by Django 5.0.1 on 2024-03-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0011_manageproject_featured_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageproject',
            name='featured_img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project_review',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unliked Post'), ('Like', 'Liked Post')], max_length=200),
        ),
    ]
