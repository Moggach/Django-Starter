from django.urls import path

from . import views

urlpatterns = [
    path('shows', views.shows, name="shows"),
    path('<int:show_id', views.show, name="show"),
]