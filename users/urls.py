from django.urls import path

from .views import ListUser, DetailUser


urlpatterns = [
    path("<int:pk>/", DetailUser.as_view(), name="user_detail"),
    path("", ListUser.as_view(), name="user_list"),
]
