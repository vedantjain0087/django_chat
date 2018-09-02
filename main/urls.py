from django.conf.urls import include, url
from . import views
from django.views.generic import DetailView,ListView
from main.models import User
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^new_msg/', views.new_msg, name='new_msg'),
    url(r'^add_chat/', views.add_chat, name='add_chat'),
    url(r'^all_msg/', views.all_msg, name='all_msg'),

]
