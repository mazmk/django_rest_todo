from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', viewsets.UserViewSet)
urlpatterns = router.urls
