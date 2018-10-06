# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0017_auto_20160725_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='germline_snp',
            name='end',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='start',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='somatic_snp',
            name='end',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='somatic_snp',
            name='start',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
