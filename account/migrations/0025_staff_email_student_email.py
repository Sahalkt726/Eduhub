# Generated by Django 5.0.1 on 2024-03-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_delete_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]