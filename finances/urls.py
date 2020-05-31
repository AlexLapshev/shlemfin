from django.urls import path
from . import views

urlpatterns = [
    path('', views.finances, name='finances'),
    path('sendto/', views.send_to, name='send_to')
]
