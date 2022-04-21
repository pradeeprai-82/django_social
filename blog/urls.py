from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:id>', views.post, name='blog_post'),
    path('contact', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('signup', views.SignUp, name="signup" )

]
