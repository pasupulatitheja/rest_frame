from django.urls import path

from app import views

urlpatterns = [
    path('api/',views.EmplyeeCBV.as_view())
]