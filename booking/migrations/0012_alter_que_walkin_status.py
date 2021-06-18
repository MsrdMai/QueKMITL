# Generated by Django 3.2.3 on 2021-06-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_que_walkin_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='que_walkin',
            name='status',
            field=models.CharField(choices=[('1', 'wait'), ('2', 'delete'), ('3', 'using'), ('4', 'done')], default='1', max_length=2),
        ),
    ]
