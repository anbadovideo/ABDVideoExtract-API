# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0004_auto_20150226_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekisu',
            name='video',
            field=models.OneToOneField(to='VideoEkisu.Video'),
            preserve_default=True,
        ),
    ]
