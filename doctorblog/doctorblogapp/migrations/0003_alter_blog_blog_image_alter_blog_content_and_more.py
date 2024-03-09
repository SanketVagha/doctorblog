# Generated by Django 4.2.4 on 2024-03-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorblogapp', '0002_user_password_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, default=None, max_length=1000, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]