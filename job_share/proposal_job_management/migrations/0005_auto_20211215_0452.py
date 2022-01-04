# Generated by Django 3.2 on 2021-12-15 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal_job_management', '0004_job_proposal_proposal_expired_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_proposal',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='job_proposal',
            name='proposal_expired_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 4, 52, 50, 111305)),
        ),
    ]