from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    # ajax request and response view
    path('contact/', views.contact_view, name='contact'),
]