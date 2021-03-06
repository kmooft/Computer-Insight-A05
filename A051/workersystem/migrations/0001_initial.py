# Generated by Django 3.0.2 on 2020-01-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('wear_hat_confidence', models.DecimalField(blank=True, decimal_places=4, max_digits=4, null=True)),
                ('most_close_worker_id', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
                ('isread', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'records',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.TextField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
                ('face_feature', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'workers',
                'managed': False,
            },
        ),
    ]
