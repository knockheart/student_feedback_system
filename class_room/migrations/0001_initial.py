# Generated by Django 3.2.18 on 2023-05-07 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0003_alter_semester_year'),
        ('users', '0004_auto_20230430_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.branch')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.college')),
                ('professor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.professor')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.semester')),
            ],
        ),
    ]
