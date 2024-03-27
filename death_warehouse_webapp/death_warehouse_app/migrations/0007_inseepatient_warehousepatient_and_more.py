# Generated by Django 4.2.6 on 2024-03-27 21:20

import death_warehouse_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('death_warehouse_app', '0006_alter_recherchepatient_date_deces'),
    ]

    operations = [
        migrations.CreateModel(
            name='INSEEPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(db_index=True, max_length=100)),
                ('prenom', models.TextField(max_length=100)),
                ('date_naiss', death_warehouse_app.models.CustomDateField(db_index=True)),
                ('pays_naiss', models.CharField(blank=True, max_length=100)),
                ('lieu_naiss', models.CharField(blank=True, max_length=100)),
                ('code_naiss', models.CharField(blank=True, max_length=10)),
                ('date_deces', death_warehouse_app.models.CustomDateField(blank=True, default='1970-01-01', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehousePatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PATIENT_NUM', models.CharField(max_length=50, null=True)),
                ('LASTNAME', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('FIRSTNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('BIRTH_DATE', models.DateField(db_index=True, null=True)),
                ('SEX', models.CharField(blank=True, max_length=10, null=True)),
                ('MAIL', models.CharField(blank=True, max_length=100, null=True)),
                ('MAIDEN_NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('DEATH_DATE', models.DateField(blank=True, null=True)),
                ('BIRTH_COUNTRY', models.CharField(blank=True, max_length=50, null=True)),
                ('HOSPITAL_PATIENT_ID', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='RecherchePatient',
        ),
    ]
