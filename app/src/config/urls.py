from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auction/', include('auction.urls')),
    path('api/v1/base-auth', include('rest_framework.urls')),
    path('api/v1/auth', include('djoser.urls')),
    path('api/v1/auth_token', include('djoser.urls.authtoken')),
]
