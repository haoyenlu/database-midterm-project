from django.urls import path
from api import views


urlpatterns = [
    path('beach_search',views.beach_search),
    path('town_list',views.town_list),
    path('beach_information',views.beach_information),
]