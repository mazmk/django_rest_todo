from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_post_todos, name='get-all-todos-create-todo'),
    path('<str:primary_key>', views.upd_dlt_todos, name='update-delete-todo'),
]