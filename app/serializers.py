from rest_framework import serializers

from . import models


class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = [
            'phone_number',
            'gender',
            'username',
            'password',
        ]


class CategoryModelSerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = models.Category
        fields = ['id', 'name']

    # def get_children(self, obj):
    #     return CategoryModelSerializer(obj.get_children(), many=True).data


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(many=True)

    class Meta:
        model = models.Product
        fields = [
            'name',
            'price',
            'image',
            'category',
            'description',
            'slug',
        ]


class CartModelSerializer(serializers.ModelSerializer):
    customer = CustomerModelSerializer(read_only=True)

    class Meta:
        model = models.Cart
        fields = ['id', 'customer', 'created_at']


class CartItemModelSerializer(serializers.ModelSerializer):
    # hffg = serializers.SerializerMethodField()

    class Meta:
        model = models.CartItem
        fields = [
            'cart',
            'product',
            'quantity',
            'created_at',
        ]


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'


class CustomerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=16)
