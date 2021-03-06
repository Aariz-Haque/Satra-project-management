# Generated by Django 4.0.1 on 2022-03-27 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_beneficiary_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='screeningcamp',
            name='blood_pressure',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='screeningcamp',
            name='date_of_camp',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screeningcamp',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='screeningcamp',
            name='prescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='screeningcamp',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
