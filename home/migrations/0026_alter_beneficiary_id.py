# Generated by Django 4.0.1 on 2022-03-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_screeningcamp_dob_alter_screeningcamp_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
