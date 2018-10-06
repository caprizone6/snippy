# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0009_remove_csvfile_submitter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csvfile',
            old_name='result',
            new_name='germline_result',
        ),
        migrations.AddField(
            model_name='csvfile',
            name='somatic_result',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
