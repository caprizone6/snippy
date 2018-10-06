# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0014_auto_20160725_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='germline_snp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(default=None, max_length=100)),
                ('chromosome', models.CharField(default=None, max_length=5)),
                ('start', models.IntegerField(default=None)),
                ('end', models.IntegerField(default=None)),
                ('ref_allele', models.CharField(default=None, max_length=30)),
                ('alt_allele', models.CharField(default=None, max_length=30)),
                ('variant_class', models.CharField(default=None, max_length=30)),
                ('variant_type', models.CharField(default=None, max_length=30)),
                ('ensemblID', models.CharField(default=None, max_length=30)),
                ('study_name', models.ForeignKey(to='oncotator.CSVFile', null=None)),
            ],
        ),
        migrations.CreateModel(
            name='somatic_snp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(default=None, max_length=100)),
                ('chromosome', models.CharField(default=None, max_length=5)),
                ('start', models.IntegerField(default=None)),
                ('end', models.IntegerField(default=None)),
                ('ref_allele', models.CharField(default=None, max_length=30)),
                ('alt_allele', models.CharField(default=None, max_length=30)),
                ('variant_class', models.CharField(default=None, max_length=30)),
                ('variant_type', models.CharField(default=None, max_length=30)),
                ('ensemblID', models.CharField(default=None, max_length=30)),
                ('study_name', models.ForeignKey(to='oncotator.CSVFile', null=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='germline_snps',
            name='study_name',
        ),
        migrations.RemoveField(
            model_name='somatic_snps',
            name='study_name',
        ),
        migrations.DeleteModel(
            name='germline_snps',
        ),
        migrations.DeleteModel(
            name='somatic_snps',
        ),
    ]
