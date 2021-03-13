from rest_framework import routers

from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Le Bazaar",
      default_version='v21.03',
      description="Api for react and flutter",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('category', views.CategoryModelViewSet)
router.register('registration', views.CustomerModelViewSet, basename='registration')
router.register('product', views.ProductModelViewSet)
router.register('cart', views.CartModelViewSet)
router.register('cart-item', views.CartItemModelViewSet)
# router.register('order', views.OrderModelViewSet)
# router.register('order-item', views.OrderItemModelViewSet)
router.register('banner', views.BannerModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginViewGenericAPIView.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
