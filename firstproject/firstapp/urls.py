from django.urls import path
from . import views

urlpatterns = [
    path('',views.journey,name="journey"), 
    path('chai_stores/',views.chai_store,name="chaistores"), 
]