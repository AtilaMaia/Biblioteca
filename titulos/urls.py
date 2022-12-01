from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:titulo_id>',views.specs, name='specs'),
]
