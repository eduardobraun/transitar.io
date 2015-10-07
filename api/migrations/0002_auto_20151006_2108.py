# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='osm_data',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='node',
            name='state',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'D', b'Deleted'), (b'A', b'Active'), (b'R', b'Review')]),
        ),
    ]
