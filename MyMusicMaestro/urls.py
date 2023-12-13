from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Defining the URL patterns for the application
urlpatterns = [
                  path('', include('app_pages.urls')),
                  path('albums/', include('app_album_viewer.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
