from rest_framework import serializers
from App_Inventory import models 

class JSONSerializerField(serializers.Field):

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = '__all__'

class AttributeTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttributeTerm
        fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = '__all__'

class SingleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['title'] = instance.name
        response['key'] = instance.id
        response['value'] = instance.id
        return response

class CategorySerializer(serializers.ModelSerializer):
    # your_conditional_field = serializers.SerializerMethodField()
    data = JSONSerializerField()
    children = serializers.SerializerMethodField(read_only=True)
    # parent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'

    def get_children(self, obj):
        # query what your want here.
        # print(obj)
        category = models.Category.objects.filter(Category_parent=obj)
        if category is not None:
            return CategorySerializer(category, many=True).data
        else:
            return None

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['title'] = instance.name
        response['key'] = instance.id
        response['value'] = instance.id
        response['immediate_parent'] = SingleCategorySerializer(
            instance.Category_parent).data
        # response['response'] = response

        return response


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Items
        fields = '__all__'

class ItemVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemVariation
        fields = '__all__'

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemImage
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = '__all__'

