from django.urls import path

from . import views
from django.views.generic.base import TemplateView # new

# indexs for html pages linked to methods views. something
urlpatterns = [
    path('', views.index, name='index'),
    path('name/data/', views.index2, name='index2'),
    path('name/', views.get_name, name='get_name'),
    path('scatter/', views.demo_scatter, name='demo_scatter'),
    # path('tester/', views.test, name='test'),
    path('/login', TemplateView.as_view(template_name='home.html'), name='home'),  # new

]
