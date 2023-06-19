from django.urls import path
from .api import user_api_view, user_detail_api_view

urlpatterns = [
    path('usuario/', user_api_view, name="usuario"),
    path('usuario/<int:user_id>', user_detail_api_view, name="detalle-usuario"),
]
