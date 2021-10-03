# Generated by Django 2.1.7 on 2019-03-31 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import private_storage.fields
import private_storage.storage.files
import submissions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('verdict', models.CharField(blank=True, default='...', max_length=50)),
                ('execution_time', models.PositiveIntegerField(blank=True, null=True)),
                ('memory', models.PositiveIntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, choices=[('text', 'Plain Text'), ('c_cpp', 'C++'), ('java', 'Java')], default='c_cpp', max_length=100)),
                ('actual_language', models.CharField(blank=True, max_length=100)),
                ('solution', private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=submissions.models.user_directory_path)),
                ('sidno', models.PositiveIntegerField(blank=True, null=True)),
                ('problem_submitted', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='problem_m_submission', to='problems.Problem')),
                ('user_handle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_m_submission', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(blank=True, choices=[('text', 'Plain Text'), ('c_cpp', 'C++'), ('java', 'Java')], default='c_cpp', max_length=100)),
                ('actual_language', models.CharField(blank=True, max_length=100)),
                ('solution', private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=submissions.models.user_directory_path)),
                ('sidno', models.PositiveIntegerField(blank=True, null=True)),
                ('problem_submitted', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='problem_c_submission', to='problems.Problem')),
                ('user_handle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_c_submission', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
