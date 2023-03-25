# Generated by Django 3.2.18 on 2023-03-25 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
        ('users', '0002_professor_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.branch'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='college_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.college'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.branch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='college_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.college'),
        ),
    ]