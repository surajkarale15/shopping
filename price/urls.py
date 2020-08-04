from django.contrib import admin
from django.urls import path
from price.views import *


'''
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'customers', CustomerOp)
urlpatterns = router.urls

'''


urlpatterns = [
    # path('', welcome),
    path('pri_welcome/', welcome_price_page),
    path('pri_persist/', save_or_update),
    path("pri_delete/<int:pid>",delete_price),
    path("pri_edit/<int:pid>",fetch_price)
]
