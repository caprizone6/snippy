from django.contrib import admin
from .models import CSVFile

class FileAdmin(admin.ModelAdmin):
	list_display = ['title', 'file', 'result', 'upload_time']

admin.site.register(CSVFile, FileAdmin)
