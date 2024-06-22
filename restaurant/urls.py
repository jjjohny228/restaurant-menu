from django.urls import path, include
from rest_framework import routers
from restaurant.views import RestaurantModelViewSet, MenuModelViewSet

app_name = 'restaurant'

router = routers.DefaultRouter()
router.register('restaurants', RestaurantModelViewSet)
router.register('menus', MenuModelViewSet)

urlpatterns = [path('', include(router.urls))]
