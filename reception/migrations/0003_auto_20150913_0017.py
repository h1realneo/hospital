# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_auto_20150913_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blankreception',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
