# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0004_auto_20150913_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blankreception',
            old_name='day',
            new_name='date',
        ),
        migrations.AlterUniqueTogether(
            name='blankreception',
            unique_together=set([('doctor', 'date', 'time')]),
        ),
    ]
