# Generated by Django 3.2.3 on 2021-06-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeQue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_type_que', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'type_que',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TypeUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_type_user', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'type_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Week_Day',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_day', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'week_day',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='QueInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_que', models.CharField(max_length=50)),
                ('prefix', models.CharField(max_length=2)),
                ('date_start', models.DateField(null=True)),
                ('date_end', models.DateField(null=True)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('wait_time', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'unfinished'), ('2', 'done')], default='1', max_length=2)),
                ('day_open', models.ManyToManyField(to='provider.Week_Day')),
                ('type_que', models.ManyToManyField(to='provider.TypeQue')),
                ('type_user', models.ManyToManyField(to='provider.TypeUser')),
            ],
            options={
                'db_table': 'queinfo',
                'managed': True,
            },
        ),
    ]