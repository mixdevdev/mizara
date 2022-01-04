# Generated by Django 3.2 on 2021-12-12 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_contract_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Designation')),
                ('description', models.TextField(verbose_name='Desc')),
            ],
        ),
        migrations.CreateModel(
            name='Job_proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_ref', models.CharField(max_length=200)),
                ('city_region', models.CharField(max_length=200, verbose_name='Ville / Region')),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='proposal_job_management.job_contract_type')),
            ],
        ),
    ]