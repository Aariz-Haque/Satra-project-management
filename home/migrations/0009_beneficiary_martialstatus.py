# Generated by Django 4.0.1 on 2022-02-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_beneficiary_familymonthlyincome'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='martialStatus',
            field=models.CharField(blank=True, choices=[('unmarried', 'UNMARRIED'), ('married', 'MARRIED'), ('separated', 'SEPARATED'), ('widow', 'WIDOW'), ('remarried', 'REMARRIED')], max_length=200, null=True),
        ),
    ]
