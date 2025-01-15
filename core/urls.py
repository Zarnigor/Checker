from django.contrib import admin
from django.urls import path, include
from app.router import router_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_urls))
]
