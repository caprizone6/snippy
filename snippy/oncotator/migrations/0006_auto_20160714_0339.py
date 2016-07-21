# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0005_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='csvfile',
            name='file',
            field=models.FileField(default=datetime.datetime(2016, 7, 14, 3, 39, 3, 223171, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
