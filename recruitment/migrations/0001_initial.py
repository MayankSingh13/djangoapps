# Generated by Django 3.1.3 on 2021-07-07 06:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=30)),
                ('parent_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=12)),
                ('category', models.CharField(max_length=15)),
                ('mob_no', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('email', models.EmailField(max_length=60)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
    ]