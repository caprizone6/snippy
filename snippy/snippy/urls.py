from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    url(r'^$', 'snippy.views.index', name='index'),
    url(r'^tools/', 'snippy.views.tools', name='tools'),
    url(r'^works/', 'snippy.views.works', name='works'),
    url(r'^contact/', 'snippy.views.contact', name='contact'),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^signup/', 'snippy.views.signup', name='signup'),
    url(r'^snp_tools/', 'oncotator.views.file_form', name='file_form'),
    url(r'^logout/', 'snippy.views.logout_view', name='logout'),
    url(r'^result/', 'oncotator.views.result', name='result'),
    url(r'^signup_form/', 'snippy.views.signup_form', name='signup_form'),
    url(r'^accounts/profile/', 'oncotator.views.result', name='result'),
    url(r'^snp_detail/(?P<id>\d+)/', 'oncotator.views.snp_detail', name='snp_detail'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)