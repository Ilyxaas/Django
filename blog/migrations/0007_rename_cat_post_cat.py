# Generated by Django 4.0.5 on 2022-07-18 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Cat',
            new_name='cat',
        ),
    ]
