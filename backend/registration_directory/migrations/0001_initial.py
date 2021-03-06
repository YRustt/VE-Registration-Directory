# Generated by Django 2.2 on 2020-08-25 11:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import registration_directory.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=1024, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=registration_directory.utils.rename)),
                ('main_departments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinate_departments', to='registration_directory.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(db_index=True, max_length=256)),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('patronymic', models.CharField(db_index=True, max_length=256)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=64, null=True, validators=[django.core.validators.RegexValidator(regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('mobile_phone', models.CharField(blank=True, max_length=64, null=True, validators=[django.core.validators.RegexValidator(regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=registration_directory.utils.rename)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='registration_directory.Department')),
            ],
        ),
    ]
