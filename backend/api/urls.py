from django.urls import path
from api import views


urlpatterns = [
    path('search',views.beach_search),
]