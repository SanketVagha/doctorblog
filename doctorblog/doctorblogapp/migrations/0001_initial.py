# Generated by Django 4.2.4 on 2024-03-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=122)),
                ('blog_image', models.ImageField(blank=True, default=None, max_length=122, upload_to='upload/')),
                ('summary', models.CharField(max_length=122)),
                ('content', models.CharField(max_length=122)),
                ('status', models.IntegerField(default=1)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorblogapp.categories')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorblogapp.user')),
            ],
        ),
    ]
