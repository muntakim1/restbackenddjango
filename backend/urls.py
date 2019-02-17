from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import productViewset,index
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('product', productViewset)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                path('',index,name='index'),
                path('api-token-auth/',views.obtain_auth_token,name="api-token-auth")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
