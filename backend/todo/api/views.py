from rest_framework import generics, viewsets, permissions
from todoapp.models import Todo
from .serializers import UserSerializer, TodoSerializer, AuthRequestSerializer, LoginRequestSerializer, CommonResponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TodoListView(generics.ListCreateAPIView):
    """
        API endpoint that allows users to read and modify todos
    """
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class AuthView(APIView):
    """
        User login
    """
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=AuthRequestSerializer,
    )
    def post(self, request, format=None):
        print(request.data)
        try:
            user = User.objects.get(username=request.data['name'], email=request.data['email'])
            token = Token.objects.get(user=user)
        except Exception as e:
            print(str(e))
            user = User()
            user.username = request.data['name']
            user.email = request.data['email']
            user.is_active = True
            user.set_password = '12345678'
            user.save()
            token = Token.objects.create(user=user)

        return Response({
            'token': token.key,
            'agent': request.META['HTTP_USER_AGENT'],
            'user': '{....}'
        })


    # @swagger_auto_schema(
    #     request_body=LoginRequestSerializer,
    #     responses={200: CommonResponseSerializer}
    # )
    # def post(self, request):
    #     return Response(CommonResponseSerializer(
    #         {
    #             'status': 0,
    #             'message': 'OK'
    #         }
    #     ).data)


# class HelloView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
