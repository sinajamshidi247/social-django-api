# Generated by Django 3.0 on 2020-08-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creared',
            new_name='created',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=None, max_length=400),
        ),
    ]