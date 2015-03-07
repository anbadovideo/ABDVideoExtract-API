# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0005_auto_20150305_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekisu',
            name='duration',
            field=models.IntegerField(verbose_name='엑기스시간', default=0),
            preserve_default=True,
        ),
    ]
