from rest_framework import routers
from .ecommerce import views.ListShoppingCartAView, views.ListShoppingCartBView

router = routers.DefaultRouter()
router.register(r'ShopA', ListShoppingCartAView)
router.register(r'ShopB', ListShoppingCartBView)
