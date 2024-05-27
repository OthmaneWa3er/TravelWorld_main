from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Morocco',views.Morocco.as_view(),name='Morocco'),
    path('Brazil',views.Brazil.as_view(),name='Brazil'),
    path('destinations', views.destinations, name='destinations'),
    path('', views.index, name='index'),
    path('marseille/', views.marseille, name='marseille'),
    path('travel/', views.travel, name='travel'),
    path('travel2/', views.travel2, name='travel2'),
]