# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0011_auto_20150318_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='arn',
            field=models.CharField(max_length=2048, verbose_name='arn', blank=True, default=''),
            preserve_default=True,
        ),
    ]
