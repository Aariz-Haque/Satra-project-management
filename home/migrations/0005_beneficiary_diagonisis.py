# Generated by Django 4.0.1 on 2022-02-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_beneficiary_email_beneficiary_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='diagonisis',
            field=models.CharField(choices=[('bipolar', 'BIPOLAR'), ('schizophrenia', 'SCHIZOPHRENIA'), ('depression', 'DEPRESSION'), ('mania', 'MANIA'), ('anxiety disorders', 'ANXIETY DISORDERS'), ('panic disorder', 'PANIC DISORDER'), ('stress-related disorders', 'STRESS-RELATED DISORDERS'), ('dissociative disorders', 'DISSOCIATIVE DISORDERS'), ('dissociative amnesia', 'DISSOCIATIVE AMNESIA'), ('somatic symptom disorder', 'SOMATIC SYMPTOM DISORDER'), ('insomnia disorder', 'INSOMNIA DISORDER'), ('substance-related disorders', 'SUBSTANCE-RELATED DISORDERS'), ('obsessive-compulsive disorders (ocd)', 'OBSESSIVE-COMPULSIVE DISORDERS (OCD)'), ('personality disorders', 'PERSONALITY DISORDERS'), ('paranoid personality disorder', 'PARANOID PERSONALITY DISORDER'), ('other', 'OTHER')], default='depression', max_length=200),
            preserve_default=False,
        ),
    ]
