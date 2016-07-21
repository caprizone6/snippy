# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0002_auto_20160713_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 7, 13, 20, 15, 44, 545203, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
