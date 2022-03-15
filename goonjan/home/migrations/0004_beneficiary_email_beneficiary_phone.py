# Generated by Django 4.0.1 on 2022-02-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_beneficiary_addresstype_beneficiary_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
