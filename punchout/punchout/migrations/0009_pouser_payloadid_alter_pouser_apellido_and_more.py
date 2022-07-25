# Generated by Django 4.0.6 on 2022-07-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchout', '0008_pouser_concurrentsessions'),
    ]

    operations = [
        migrations.AddField(
            model_name='pouser',
            name='payloadID',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='apellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='businessunit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='buyercookie',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='nombre_unico',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='secretID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='urlToRedirect',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pouser',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]