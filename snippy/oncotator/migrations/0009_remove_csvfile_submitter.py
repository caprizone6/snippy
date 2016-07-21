# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0008_auto_20160717_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='submitter',
        ),
    ]
