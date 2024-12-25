from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from ghsystems.apps.api.auth import urls as auth_urls
from ghsystems.apps.api.tasks import urls as tasks_urls


app_name = 'api'

urlpatterns = [
    path('auth/', include(auth_urls, namespace='auth')),
    path('tasks/', include(tasks_urls, namespace='tasks')),
]

docs_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]

urlpatterns += docs_urlpatterns
