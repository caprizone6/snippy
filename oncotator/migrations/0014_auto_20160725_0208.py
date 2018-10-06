# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0013_auto_20160725_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='germline_snps',
            old_name='result_file',
            new_name='study_name',
        ),
        migrations.RenameField(
            model_name='somatic_snps',
            old_name='result_file',
            new_name='study_name',
        ),
    ]
