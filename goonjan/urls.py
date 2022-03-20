from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.i18n import JavaScriptCatalog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header  =  "Satra admin"  
admin.site.site_title  =  "Satra Admin Portal"
admin.site.index_title  =  "Welcome to Satra admin portal"