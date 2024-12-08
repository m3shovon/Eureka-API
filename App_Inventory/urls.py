from django.urls import path, include
from rest_framework.routers import DefaultRouter
from App_Inventory  import views

router = DefaultRouter()
router.register(r'attributes', views.AttributeViewSet)
router.register(r'attribute-terms', views.AttributeTermViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'items', views.ItemsViewSet)
router.register(r'item-variations', views.ItemVariationViewSet)
router.register(r'item-images', views.ItemImageViewSet)
router.register(r'services', views.ServicesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]