from django.contrib import admin
from django.urls import include, path
from demo import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('boilerplate.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
