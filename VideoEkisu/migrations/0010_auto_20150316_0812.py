# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0009_auto_20150313_0205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ekisu',
            options={'ordering': ['-created'], 'verbose_name': '엑기스'},
        ),
    ]
