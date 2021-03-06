
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/shop/', include('shop.urls')),
    path('api/shop/orders/', include('order.urls')),
    path('api/shop/lineitem/', include('lineitem.urls')),
]
