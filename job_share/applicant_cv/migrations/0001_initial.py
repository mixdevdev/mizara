# Generated by Django 3.2 on 2021-12-27 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('path_linkedin', models.CharField(max_length=200)),
                ('birth_date', models.DateTimeField()),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='curriculum_degree', to='applicant_cv.degree')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='curriculum_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]