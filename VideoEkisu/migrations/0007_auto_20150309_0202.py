# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0006_ekisu_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ekisu',
            name='video',
            field=models.ForeignKey(verbose_name='엑기스', to='VideoEkisu.Video'),
            preserve_default=True,
        ),
    ]
