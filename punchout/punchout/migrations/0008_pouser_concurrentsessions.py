# Generated by Django 4.1 on 2022-07-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchout', '0007_pouser_sessionexpiredat_pouser_sessionopen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pouser',
            name='concurrentSessions',
            field=models.IntegerField(null=True),
        ),
    ]