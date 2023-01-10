from .import views
from django.urls import path,include
urlpatterns = [
    path('',views.index,name='home'),
    path('user_login',views.userlogin,name='userlogin'),
    path('register',views.signup,name='signup'),
    path('newpage',views.resgiter,name='newpage')
    
]