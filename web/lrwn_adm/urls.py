from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

# dev imports
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# dev static files TODO remove for production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)