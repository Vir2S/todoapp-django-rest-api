from todoapp import models
from rest_framework import serializers
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField()
    title = serializers.CharField(max_length=250)
    text = serializers.CharField()
    complete = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return models.Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.complete = validated_data.get('complete', instance.complete)
        instance.save()
        return instance

    class Meta:
        model = models.Todo
        fields = ['id', 'due_date', 'title', 'text', 'complete']


class CommonResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'email',
            # 'first_name',
            # 'last_name',
            'is_staff',
        ]


class AuthRequestSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    auth_token = serializers.CharField()
