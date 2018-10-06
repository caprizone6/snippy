# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0012_auto_20160725_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='germline_snps',
            name='variant_calss',
        ),
        migrations.RemoveField(
            model_name='somatic_snps',
            name='variant_calss',
        ),
        migrations.AddField(
            model_name='germline_snps',
            name='variant_class',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='somatic_snps',
            name='variant_class',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='alt_allele',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='chromosome',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='end',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='ensemblID',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='gene',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='ref_allele',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='result_file',
            field=models.ForeignKey(to='oncotator.CSVFile', null=None),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='start',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='germline_snps',
            name='variant_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='alt_allele',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='chromosome',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='end',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='ensemblID',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='gene',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='ref_allele',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='result_file',
            field=models.ForeignKey(to='oncotator.CSVFile', null=None),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='start',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='somatic_snps',
            name='variant_type',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
