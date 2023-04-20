# Generated by Django 4.2 on 2023-04-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='content',
            new_name='contents',
        ),
        migrations.RemoveField(
            model_name='content',
            name='parent_channel',
        ),
        migrations.RemoveField(
            model_name='subchannel',
            name='parent_channel',
        ),
        migrations.AlterField(
            model_name='content',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
