from django.contrib import admin
from restaurant.models import Restaurant, Menu

admin.site.register([Restaurant, Menu])
