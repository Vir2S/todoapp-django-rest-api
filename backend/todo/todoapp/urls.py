from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add_todo'),
    path('complete/<todo_id>', views.complete_todo, name='complete_todo'),
    path('deletecompleted', views.delete_completed, name='delete_completed'),
    path('deleteall', views.delete_all, name='delete_all'),
]
