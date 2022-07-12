from django.urls import path
from . import views

urlpatterns = [
    path('api/supers', views.get_all_supers)
]