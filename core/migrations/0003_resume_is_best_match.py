# Generated by Django 5.2.1 on 2025-05-22 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_resume_context_score_resume_education_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='is_best_match',
            field=models.BooleanField(default=False),
        ),
    ]
