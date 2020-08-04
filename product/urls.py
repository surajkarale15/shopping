from django.contrib import admin
from django.urls import path
from product.views import *


'''
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'customers', CustomerOp)
urlpatterns = router.urls

'''


urlpatterns = [
    # path('', welcome),
    path('prod_welcome/', welcome_product_page),
    path('prod_persist/', save_or_update),
    path("prod_delete/<int:pid>",delete_product),
    path("prod_edit/<int:pid>",fetch_product)
]
