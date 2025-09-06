
from django.urls import path
from .views import HomeView, AboutView, Services, Menu, Booking, Ourteam, Testimonials, ContactView
urlpatterns = [

    path('home/', HomeView.as_view(), name='home_view'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('services/', Services.as_view(), name='services_view'),
    path('menu/', Menu.as_view(), name='menu_view'),
    path('booking/', Booking.as_view(), name='booking_view'),
    path('team/', Ourteam.as_view(), name='team_view'),
    path('testimonials/', Testimonials.as_view(), name='testimonials_view'),
    path('contact/', ContactView.as_view(), name='contact_view'),
]