from .import views
from django.urls import path


urlpatterns =[
    path('', views.home, name='home'),
    path('seat/', views.seat, name='seat'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('available/', views.available, name='available'),
]