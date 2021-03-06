# Generated by Django 4.0.1 on 2022-03-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_beneficiary_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screeningcamp',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screeningcamp',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='screeningcamp',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
