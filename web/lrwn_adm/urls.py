from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

# dev imports
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from web.catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# dev static files TODO remove for production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
