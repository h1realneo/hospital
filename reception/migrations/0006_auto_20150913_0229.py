# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0005_auto_20150913_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blankreception',
            name='name_patient',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='blankreception',
            name='patronymic_patient',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='blankreception',
            name='surname_patient',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
