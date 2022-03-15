# Generated by Django 4.0.1 on 2022-02-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_beneficiary_durationofillness'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='pastPyschiatricIllness',
            field=models.CharField(blank=True, choices=[('absent', 'ABSENT'), ('present', 'PRESENT'), ('unclear', 'UNCLEAR')], max_length=200, null=True),
        ),
    ]