# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ekisu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='제목', max_length=256)),
                ('section', models.TextField(verbose_name='구간', max_length=2048)),
                ('created', models.DateTimeField(verbose_name='생성일', auto_now_add=True)),
            ],
            options={
                'verbose_name': '엑기스',
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='제목', max_length=512)),
                ('thumbnail', models.CharField(verbose_name='썸네일', max_length=1024)),
                ('view_count', models.IntegerField(verbose_name='조회수', default=0)),
                ('duration', models.IntegerField(verbose_name='재생시간')),
            ],
            options={
                'verbose_name': '동영상',
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ekisu',
            name='video_id',
            field=models.ForeignKey(verbose_name='엑기스', to='VideoEkisu.Video'),
            preserve_default=True,
        ),
    ]
