# Generated by Django 3.1.4 on 2021-02-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='visitor', max_length=255),
            preserve_default=False,
        ),
    ]