# Generated by Django 3.2.18 on 2023-03-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_to_professors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacktoprofessors',
            name='semester',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktoprofessors',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
