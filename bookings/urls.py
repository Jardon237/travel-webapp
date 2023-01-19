from .import views
from django.urls import path


urlpatterns =[
    path('', views.home, name='home'),
    path('seat/', views.seat, name='seat.html'),
    path('signup/', views.signup, name='signup.html'),
    path('signin/', views.signin, name='signin.html'),
    path('available/', views.available, name='available.html'),
]