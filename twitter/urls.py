from django.urls import path
from twitter import views

urlpatterns = [
    path('', views.index, name='twitter-index'),
    path('profile/<str:account>', views.profile, name='twitter-profile'),
]
