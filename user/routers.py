from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.viewsets import SignUp, ActivateUser

router = routers.DefaultRouter()
# router.register("signup", SignUpViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("login/", LoginViewSet.as_view()),
    path("signup/", SignUp.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/', ActivateUser.as_view(), name='activate_user'),

]
