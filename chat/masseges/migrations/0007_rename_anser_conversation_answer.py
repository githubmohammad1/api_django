# Generated by Django 5.0.4 on 2024-05-27 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masseges', '0006_rename_anser_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='anser',
            new_name='answer',
        ),
    ]
