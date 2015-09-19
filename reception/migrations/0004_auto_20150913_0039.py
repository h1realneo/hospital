# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_auto_20150913_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blankreception',
            name='id',
            field=models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID'),
        ),
    ]
