# Generated by Django 4.0.5 on 2022-07-05 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='Cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
    ]
