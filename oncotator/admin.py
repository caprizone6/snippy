from django.contrib import admin
from .models import CSVFile, germline_snp, somatic_snp

class FileAdmin(admin.ModelAdmin):
	list_display = ['title', 'file', 'somatic_result', 'germline_result', 'user', 'upload_time']

class gSnpAdmin(admin.ModelAdmin):
    list_display = ['study_name', 'gene', 'chromosome', 'start', 'end', 'ref_allele','alt_allele', 'ensemblID']

class sSnpAdmin(admin.ModelAdmin):
    list_display = ['study_name', 'gene', 'chromosome', 'start', 'end', 'ref_allele','alt_allele', 'ensemblID']

admin.site.register(CSVFile, FileAdmin)
admin.site.register(germline_snp, gSnpAdmin)
admin.site.register(somatic_snp, sSnpAdmin)
