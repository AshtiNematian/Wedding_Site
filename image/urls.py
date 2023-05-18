from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
import image.forms
import image.views
from django.contrib import admin
admin.autodiscover()

admin.autodiscover()

urlpatterns = [
                  url(r'^$', image.views.gallery, name='gallery'),
                  url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
                  url(r'^(?P<slug>[-\w]+)$', image.views.AlbumDetail.as_view(), name='album'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'image.views.handler404'
