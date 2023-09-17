# Generated by Django 3.1.4 on 2021-02-07 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gource_studio.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('project_url', models.TextField()),
                ('project_branch', models.CharField(default='master', max_length=255)),
                ('project_vcs', models.CharField(choices=[('git', 'Git'), ('hg', 'Mercurial')], default='git', max_length=16)),
                ('project_slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('project_log', models.FileField(blank=True, null=True, upload_to=gource_studio.core.models.get_project_project_log_path)),
                ('project_log_updated_at', models.DateTimeField(blank=True, null=True)),
                ('project_log_commit_hash', models.CharField(blank=True, max_length=64, null=True)),
                ('project_log_commit_time', models.DateTimeField(blank=True, null=True)),
                ('project_log_commit_preview', models.CharField(blank=True, max_length=128, null=True)),
                ('build_title', models.CharField(blank=True, default='', max_length=255)),
                ('build_logo', models.ImageField(blank=True, null=True, upload_to=gource_studio.core.models.get_project_build_logo_path)),
                ('build_audio', models.FileField(blank=True, null=True, upload_to=gource_studio.core.models.get_project_build_audio_path)),
                ('build_audio_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('queued', 'Queued'), ('canceled', 'Canceled'), ('running', 'Running'), ('aborted', 'Aborted'), ('completed', 'Completed'), ('errored', 'Errored')], default='pending', max_length=16)),
                ('project_branch', models.CharField(default='master', max_length=255)),
                ('project_log', models.FileField(blank=True, null=True, upload_to=gource_studio.core.models.get_build_project_log_path)),
                ('content', models.FileField(blank=True, null=True, upload_to=gource_studio.core.models.get_video_build_path)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to=gource_studio.core.models.get_video_screenshot_path)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=gource_studio.core.models.get_video_thumbnail_path)),
                ('duration', models.PositiveIntegerField(null=True)),
                ('size', models.PositiveIntegerField(null=True)),
                ('queued_at', models.DateTimeField(null=True)),
                ('running_at', models.DateTimeField(null=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('errored_at', models.DateTimeField(null=True)),
                ('stdout', models.FileField(blank=True, null=True, upload_to=gource_studio.core.models.get_build_stdout_path)),
                ('stderr', models.FileField(blank=True, null=True, upload_to=gource_studio.core.models.get_build_stderr_path)),
                ('error_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUserAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=gource_studio.core.models.get_project_avatar_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_project_avatars', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatars', to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=gource_studio.core.models.get_global_avatar_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_avatars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAvatarAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='core.useravatar')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUserAvatarAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='core.projectuseravatar')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCaption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('text', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captions', to='core.project')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ProjectBuildOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=1024)),
                ('value_type', models.CharField(max_length=32)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='core.projectbuild')),
            ],
        ),
    ]
