from django.urls import path, include
from api.views import AuthView, TodoListView, TodoDetailView, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth', AuthView.as_view()),
    path('todo/', TodoListView.as_view()),
    path('todo/<int:pk>/', TodoDetailView.as_view()),
]