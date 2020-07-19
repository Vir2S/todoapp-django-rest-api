from django.urls import path
from users.views import CreateUserAPIView
 
urlpatterns = [
    path('createuser/', CreateUserAPIView.as_view()),
]