from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static
from snippy.views import index, tools, works, signup, logout_view, signup_form, contact
from oncotator.views import file_form, result, somatic_gene_network, germline_gene_network, somatic_snp_detail, germline_snp_detail, SomaticReportDraft, GermlineReportDraft

# these patterns defines which page to display according to url pattern
# url pattern triggers view in particular views.py file
# e.g. /result/ will trigger "result" function from oncotator.views

urlpatterns = [
  
    url(r'^$', index, name='index'),
    url(r'^tools/', tools, name='tools'),
    url(r'^works/', works, name='works'),
    url(r'^contact/', contact, name='contact'),
    url(r'^login/', login, name='login'),
    url(r'^signup/', signup, name='signup'),
    url(r'^snp_tools/', file_form, name='file_form'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^result/', result, name='result'),
    url(r'^signup_form/', signup_form, name='signup_form'),
    url(r'^accounts/profile/', result, name='result'),
    url(r'^somatic_snp_detail/(?P<id>\d+)/', somatic_snp_detail, name='somatic_snp_detail'),
    url(r'^germline_snp_detail/(?P<id>\d+)/', germline_snp_detail, name='germline_snp_detail'),
    url(r'^somatic_report/(?P<id>\d+)/', SomaticReportDraft, name='SomaticReportDraft'),
    url(r'^germline_report/(?P<id>\d+)/', GermlineReportDraft, name='GermlineReportDraft'),
    url(r'^germline_gene_network/(?P<id>\d+)/', germline_gene_network, name='germline_gene_network'),
    url(r'^somatic_gene_network/(?P<id>\d+)/', somatic_gene_network, name='somatic_gene_network'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)