# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0010_auto_20150316_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='arn',
            field=models.CharField(default='', max_length=2048, verbose_name='arn'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ekisu',
            name='duration',
            field=models.IntegerField(default=0, editable=False, verbose_name='엑기스시간'),
            preserve_default=True,
        ),
    ]
