# Generated by Django 4.0.1 on 2022-03-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_remove_beneficiary_if_present_schizophrenia_or_mania_or_depression'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screeningcamp',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]