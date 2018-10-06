# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncotator', '0010_auto_20160723_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='germline_snps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=100)),
                ('chromosome', models.CharField(max_length=5)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('ref_allele', models.CharField(max_length=30)),
                ('alt_allele', models.CharField(max_length=30)),
                ('variant_calss', models.CharField(max_length=30)),
                ('variant_type', models.CharField(max_length=30)),
                ('result_file', models.ForeignKey(to='oncotator.CSVFile')),
            ],
        ),
        migrations.CreateModel(
            name='somatic_snps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene', models.CharField(max_length=100)),
                ('chromosome', models.CharField(max_length=5)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('ref_allele', models.CharField(max_length=30)),
                ('alt_allele', models.CharField(max_length=30)),
                ('variant_calss', models.CharField(max_length=30)),
                ('variant_type', models.CharField(max_length=30)),
                ('result_file', models.ForeignKey(to='oncotator.CSVFile')),
            ],
        ),
    ]
