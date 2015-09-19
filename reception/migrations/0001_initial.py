# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlankReception',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('name_patient', models.CharField(max_length=100)),
                ('surname_patient', models.CharField(max_length=100)),
                ('patronymic_patient', models.CharField(max_length=100)),
                ('number_patient', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blankreception',
            name='doctor',
            field=models.ForeignKey(to='reception.Doctor'),
        ),
        migrations.AlterUniqueTogether(
            name='blankreception',
            unique_together=set([('doctor', 'day', 'time')]),
        ),
    ]
