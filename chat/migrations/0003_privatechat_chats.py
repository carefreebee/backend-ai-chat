# Generated by Django 5.0.6 on 2024-05-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_groupchat_privatechat'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatechat',
            name='chats',
            field=models.ManyToManyField(related_name='private_chats', to='chat.chat'),
        ),
    ]
