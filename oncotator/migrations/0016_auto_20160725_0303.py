# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0015_auto_20160725_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='germline_snp',
            name='alt_allele',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='chromosome',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='end',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='ensemblID',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='gene',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='ref_allele',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='start',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='variant_class',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='germline_snp',
            name='variant_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
