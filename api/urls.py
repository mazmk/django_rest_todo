from django.urls import path, include
from . import views
from todos_v2.router import router

urlpatterns = [
    path('todos/', include('todos.urls')),
    path('v2/', include(router.urls)),
    path('user/', include('user.routers')),
]
