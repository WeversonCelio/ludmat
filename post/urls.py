from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('sobre/', views.sobre, name='sobre'), 
    path('post/<int:id>/', views.post, name='post'), 
]