# Generated by Django 5.0.1 on 2024-03-30 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_rename_text_question_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='text',
        ),
    ]
