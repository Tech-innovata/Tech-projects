from django.urls import path
from .import views
urlpatterns=[
    path('home/',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('homepage/',views.homepage,name='homepage'),
    path('joinus/',views.joinus_page,name='joinus')
 
]