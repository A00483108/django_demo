from django.urls import path
from .views import HotelViewSet


urlpatterns= [
    path('api/hotels/', HotelViewSet),  # Directly call the function-based view
]