# Generated by Django 5.2.1 on 2025-05-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='context_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='education_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='skill_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
