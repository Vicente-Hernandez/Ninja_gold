from django.urls import path     
from . import views


urlpatterns = [
    path('', views.home),
    path('process_money/<place>', views.process_money),
    path('reset', views.reset),
]