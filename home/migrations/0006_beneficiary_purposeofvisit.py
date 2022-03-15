# Generated by Django 4.0.1 on 2022-02-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_beneficiary_diagonisis'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='purposeOfVisit',
            field=models.CharField(blank=True, choices=[('counselling', 'COUNSELLING'), ('mental health screening', 'MENTAL HEALTH SCREENING'), ('care giver training', 'CARE GIVER TRAINING'), ('livlihood training', 'LIVILIHOOD TRAINING'), ('other', 'OTHER')], max_length=200, null=True),
        ),
    ]