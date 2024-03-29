# Generated by Django 3.2.18 on 2023-03-25 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('student_id', models.CharField(max_length=200)),
                ('student_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.branch')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.college')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('professor_id', models.CharField(max_length=200)),
                ('professor_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.branch')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.college')),
            ],
        ),
    ]
