# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0002_auto_20150225_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekisu',
            name='thumbnail',
            field=models.CharField(verbose_name='썸네일', default='', max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='identifer',
            field=models.CharField(verbose_name='identifier', default='', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='provider',
            field=models.CharField(verbose_name='제공자', default='', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.CharField(verbose_name='썸네일', default='', max_length=1024),
            preserve_default=True,
        ),
    ]
