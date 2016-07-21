# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oncotator', '0007_auto_20160714_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 17, 23, 49, 40, 737258, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='csvfile',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
