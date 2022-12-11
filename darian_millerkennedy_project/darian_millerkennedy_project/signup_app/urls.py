from django.urls import path
from . import views

urlpatterns = [path('', views.Homepage, name='Homepage'),
   path('signup', views.signup, name='signup'),
   path("contactadd", views.contactadd, name="contactadd"),
   path("signin", views.signin, name="signin"),
   path("logout", views.logout_request, name= "logout")]