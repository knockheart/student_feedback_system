# Generated by Django 3.2.18 on 2023-05-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='year',
            field=models.IntegerField(),
        ),
    ]