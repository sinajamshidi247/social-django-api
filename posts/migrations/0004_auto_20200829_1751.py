# Generated by Django 3.0 on 2020-08-29 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='POST',
            new_name='post',
        ),
    ]
