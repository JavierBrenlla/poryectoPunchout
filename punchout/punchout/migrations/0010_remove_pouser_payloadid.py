# Generated by Django 4.0.6 on 2022-07-25 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('punchout', '0009_pouser_payloadid_alter_pouser_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pouser',
            name='payloadID',
        ),
    ]