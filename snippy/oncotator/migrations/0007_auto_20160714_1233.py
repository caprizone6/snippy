# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0006_auto_20160714_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='result',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='csvfile',
            name='submitter',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
