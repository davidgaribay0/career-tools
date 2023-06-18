from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from job_hunt.views import CompanyViewSet

router = routers.DefaultRouter()
router.register('companies', CompanyViewSet)

urlpatterns = [
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/', include(router.urls)),
                  path('', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
