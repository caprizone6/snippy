from django.db import models
from django.conf import settings
from django.utils.timezone import activate

# activate(settings.TIME_ZONE)

class CSVFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    somatic_result = models.FileField(null=True)
    germline_result = models.FileField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    upload_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

class germline_snp(models.Model):
    study_name = models.ForeignKey(CSVFile, null=None)
    gene = models.CharField(max_length=100,null=True)
    chromosome = models.CharField(max_length=5,null=True)
    start = models.CharField(max_length=30, null=True)
    end = models.CharField(max_length=30, null=True)
    ref_allele = models.CharField(max_length=30, null=True)
    alt_allele = models.CharField(max_length=30, null=True)
    variant_class = models.CharField(max_length=30, null=True)
    variant_type = models.CharField(max_length=30, null=True)
    ensemblID = models.CharField(max_length=30, null=True)

class somatic_snp(models.Model):
    study_name = models.ForeignKey(CSVFile, null=None)
    gene = models.CharField(max_length=100, null=True)
    chromosome = models.CharField(max_length=5, null=True)
    start = models.CharField(max_length=30, null=True)
    end = models.CharField(max_length=30, null=True)
    ref_allele = models.CharField(max_length=30, null=True)
    alt_allele = models.CharField(max_length=30, null=True)
    variant_class = models.CharField(max_length=30, null=True)
    variant_type = models.CharField(max_length=30, null=True)
    ensemblID = models.CharField(max_length=30, null=True)
