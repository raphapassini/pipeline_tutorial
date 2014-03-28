from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', include('portal.urls', namespace='portal')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
