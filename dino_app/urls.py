from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_dinos),
    path('dino/<slug:slug_dino>', views.show_one_dino, name='dino_detail'),
]
