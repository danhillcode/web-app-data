from django.urls import path

from . import views
from django.views.generic.base import TemplateView # new


# from .views import line_chart, line_chart_json


# indexs for html pages linked to methods views. something
urlpatterns = [
    path('', views.index, name='index'),
    path('name/data/', views.index2, name='index2'),
    path('name/', views.get_name, name='get_name'),
    path('scatter/', views.demo_scatter, name='demo_scatter'),
    path('scatterStudent/', views.scatter_student, name='scatter_student'),
    path('question/', views.question, name='question'),

    # path('tester/', views.test, name='test'),
    # path('/login', TemplateView.as_view(template_name='home.html'), name='home'),  # new 

    #Pths for registration and login/signup
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('',TemplateView.as_view(template_name='home.html'), name='home'), #Loggedin user or Dashboard

]