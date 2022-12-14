# Generated by Django 4.0.5 on 2022-07-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dist',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_name', models.CharField(max_length=50)),
                ('vchr_code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('reg', models.CharField(max_length=70, unique=True)),
                ('gender', models.CharField(max_length=512)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]
