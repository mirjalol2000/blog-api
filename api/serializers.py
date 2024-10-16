from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class PostSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created', 'updated']
        # depth = 1

