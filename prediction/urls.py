# prediction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cancer-prediction/', views.cancer_prediction, name='cancer_prediction'),
]
