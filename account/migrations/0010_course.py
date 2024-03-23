# Generated by Django 5.0.1 on 2024-03-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_staff_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_image', models.ImageField(upload_to='course_images/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]