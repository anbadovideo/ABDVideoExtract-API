# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0012_auto_20150319_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='arn',
        ),
    ]
