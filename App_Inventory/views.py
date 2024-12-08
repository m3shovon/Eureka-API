from rest_framework import viewsets
from App_Inventory import models 
from App_Inventory import serializers 


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer

class AttributeTermViewSet(viewsets.ModelViewSet):
    queryset = models.AttributeTerm.objects.all()
    serializer_class = serializers.AttributeTermSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = models.Items.objects.all()
    serializer_class = serializers.ItemsSerializer

class ItemVariationViewSet(viewsets.ModelViewSet):
    queryset = models.ItemVariation.objects.all()
    serializer_class = serializers.ItemVariationSerializer

class ItemImageViewSet(viewsets.ModelViewSet):
    queryset = models.ItemImage.objects.all()
    serializer_class = serializers.ItemImageSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServicesSerializer
