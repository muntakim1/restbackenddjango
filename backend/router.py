from rest_framework import routers
from .views import productViewset
router=routers.DefaultRouter()
router.register('product',productViewset)