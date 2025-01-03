
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/auth/', include('App_Auth.urls')),
    path('api/inventory/', include('App_Inventory.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
