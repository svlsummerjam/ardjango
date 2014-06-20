from django.conf.urls import patterns, include, url
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'', IndexView.as_view(), name='index'),
                       )+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
