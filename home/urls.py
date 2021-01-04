from django.urls import path

from . import views

app_name = "playlist"
urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('remove',views.remove)
]