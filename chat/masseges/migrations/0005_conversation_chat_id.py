# Generated by Django 5.0.4 on 2024-05-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masseges', '0004_alter_conversation_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='chat_id',
            field=models.IntegerField(default=1, verbose_name=models.AutoField(primary_key=True)),
            preserve_default=False,
        ),
    ]
