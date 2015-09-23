# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('pos', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('osm_id', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('node_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='api.Node', primary_key=True)),
            ],
            bases=('api.node',),
        ),
    ]
