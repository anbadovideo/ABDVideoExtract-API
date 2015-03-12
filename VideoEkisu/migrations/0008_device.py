# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VideoEkisu', '0007_auto_20150309_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('token', models.CharField(default='', max_length=2048, verbose_name='token')),
                ('type', models.CharField(default='', max_length=256, verbose_name='type')),
            ],
            options={
                'verbose_name': '디바이스',
                'ordering': ['token'],
            },
            bases=(models.Model,),
        ),
    ]
