# Generated by Django 5.1.1 on 2024-09-16 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumemodel',
            name='award',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='codepen',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='education',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='github',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='intrest',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='language',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='resumemodel',
            name='yoursite',
        ),
    ]