# Generated by Django 3.2 on 2022-01-01 19:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proposal_job_management', '0011_delete_formation_proposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_proposal',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 1, 19, 40, 14, 144200, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
