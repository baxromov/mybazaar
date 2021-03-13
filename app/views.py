from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, response, status, permissions, views
from rest_framework import filters
from . import models
from . import serializers


class LoginViewGenericAPIView(views.APIView):
    serializer_class = serializers.CustomerLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return response.Response(status=status.HTTP_200_OK)
                else:
                    return response.Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return response.Response(status=status.HTTP_400_BAD_REQUEST)


class Logout(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return response.Response(status=status.HTTP_200_OK)


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoryModelSerializer
    queryset = models.Category.objects.filter(level=0)
    permission_classes = (permissions.AllowAny, )
    http_method_names = ['get']


class CustomerModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerModelSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = models.Customer.objects.all()
    # http_method_names = ['post']

    def get_queryset(self):
        queryset = self.queryset.filter(id=self.request.user.id)
        return queryset


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductModelSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = models.Product.objects.all()
    http_method_names = ['get']
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)

    def get_queryset(self):
        queryset = models.Product.objects.all()
        return queryset


class CartModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CartModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Cart.objects.all()


class CartItemModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CartItemModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.CartItem.objects.all()


class BannerModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BannerModelSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = models.Banner.objects.all()
    http_method_names = ['get']
