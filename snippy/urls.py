from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from snippy import views as snippy_views
from oncotator import views as oncotator_views

# these patterns defines which page to display according to url pattern
# url pattern triggers view in particular views.py file
# e.g. /result/ will trigger "result" function from oncotator.views

urlpatterns = [
  
    url(r'^$', 'snippy_views.index', name='index'),
    url(r'^tools/', 'snippy_views.tools', name='tools'),
    url(r'^works/', 'snippy_views.works', name='works'),
    url(r'^contact/', 'snippy_views.contact', name='contact'),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^signup/', 'snippy_views.signup', name='signup'),
    url(r'^snp_tools/', 'oncotator_views.file_form', name='file_form'),
    url(r'^logout/', 'snippy_views.logout_view', name='logout'),
    url(r'^result/', 'oncotator_views.result', name='result'),
    url(r'^signup_form/', 'snippy_views.signup_form', name='signup_form'),
    url(r'^accounts/profile/', 'oncotator_views.result', name='result'),
    url(r'^somatic_snp_detail/(?P<id>\d+)/', 'oncotator_views.somatic_snp_detail', name='somatic_snp_detail'),
    url(r'^germline_snp_detail/(?P<id>\d+)/', 'oncotator_views.germline_snp_detail', name='germline_snp_detail'),
    url(r'^somatic_report/(?P<id>\d+)/', 'oncotator_views.SomaticReportDraft', name='SomaticReportDraft'),
    url(r'^germline_report/(?P<id>\d+)/', 'oncotator_views.GermlineReportDraft', name='GermlineReportDraft'),
    url(r'^germline_gene_network/(?P<id>\d+)/', 'oncotator_views.germline_gene_network', name='germline_gene_network'),
    url(r'^somatic_gene_network/(?P<id>\d+)/', 'oncotator_views.somatic_gene_network', name='somatic_gene_network'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)