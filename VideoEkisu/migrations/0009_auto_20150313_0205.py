# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0008_device'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('token', 'type')]),
        ),
    ]
