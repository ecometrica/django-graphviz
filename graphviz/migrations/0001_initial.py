# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrowVisual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shape', models.CharField(default=b'normal', max_length=50, choices=[(b'box', b'box'), (b'crow', b'crow'), (b'diamond', b'diamond'), (b'dot', b'dot'), (b'inv', b'inv'), (b'none', b'none'), (b'normal', b'normal'), (b'tee', b'tee'), (b'vee', b'vee')])),
                ('modifier', models.CharField(default=b'r', max_length=1, choices=[(b'l', b'left'), (b'r', b'right'), (b'o', b'non-filled')])),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='CacheImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('valid', models.BooleanField(default=True)),
                ('file', models.ImageField(upload_to=b'graph_images')),
            ],
            options={
                'verbose_name_plural': 'Caches images',
            },
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('slug', models.SlugField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'verbose_name_plural': 'Graphes',
            },
        ),
        migrations.CreateModel(
            name='NodeVisual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('shape', models.CharField(default=b'circle', max_length=50, choices=[(b'box', b'Box'), (b'circle', b'Circle'), (b'doublecircle', b'Double circle'), (b'box3d', b'Box 3D'), (b'diamond', b'Diamond'), (b'parallelogram', b'Parallelogram')])),
                ('options', models.CharField(help_text=b'comma-separated options', max_length=100, null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('graph', models.ForeignKey(to='graphviz.Graph')),
            ],
        ),
        migrations.AddField(
            model_name='cacheimage',
            name='graph',
            field=models.ForeignKey(to='graphviz.Graph'),
        ),
        migrations.AddField(
            model_name='arrowvisual',
            name='graph',
            field=models.ForeignKey(to='graphviz.Graph'),
        ),
    ]
