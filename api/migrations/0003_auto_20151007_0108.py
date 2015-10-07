# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151006_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='osm_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
