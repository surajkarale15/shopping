from django.contrib import admin
from django.urls import path
from category.views import *


'''
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'customers', CustomerOp)
urlpatterns = router.urls

'''



urlpatterns = [
    path('', welcome),
    path('cat_welcome/', welcome_category_page),
    path('cat_persist/', save_or_update),
    path("cat_delete/<int:cid>",delete_category),
    path("cat_edit/<int:cid>",fetch_category)
]
