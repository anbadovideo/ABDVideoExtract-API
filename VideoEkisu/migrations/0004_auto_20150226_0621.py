# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0003_auto_20150225_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='identifer',
            new_name='identifier',
        ),
    ]
