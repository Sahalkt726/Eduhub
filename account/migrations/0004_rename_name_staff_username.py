# Generated by Django 5.0.1 on 2024-03-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='username',
        ),
    ]
