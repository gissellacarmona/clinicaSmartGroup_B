# Generated by Django 4.1.1 on 2022-10-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Password'),
        ),
    ]
