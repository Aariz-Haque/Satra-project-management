# Generated by Django 4.0.1 on 2022-03-28 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_rename_addresstype_beneficiary_address_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screeningcamp',
            old_name='careGiver',
            new_name='care_giver',
        ),
        migrations.RenameField(
            model_name='screeningcamp',
            old_name='fatherName',
            new_name='father_name',
        ),
        migrations.RenameField(
            model_name='screeningcamp',
            old_name='motherName',
            new_name='mother_name',
        ),
        migrations.RenameField(
            model_name='screeningcamp',
            old_name='visitedBy',
            new_name='visited_by',
        ),
        migrations.AlterField(
            model_name='screeningcamp',
            name='date_of_camp',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screeningcamp',
            name='next_review_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]