from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_v1/', include('api_v1.urls', namespace='api_v1')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
