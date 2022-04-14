from django.urls import include, path
from rest_framework import routers
from user.viewsets import LoginViewSet, SignUpViewSet

router = routers.DefaultRouter()
router.register("signup", SignUpViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginViewSet.as_view()),

]
