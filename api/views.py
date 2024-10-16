from django.shortcuts import render
from rest_framework import generics
from api.serializers import PostSerializer
from posts.models import Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import IsAuthorOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'title']
    search_fields = ['title', 'author__username']
    ordering_fields = ['username', 'created']


# class PostListView(APIView):
#
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


# class PostListAPIView(generics.ListCreateAPIView):
#     permission_classes = [
#         IsAuthenticatedOrReadOnly,
#     ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [
#         IsAuthorOrReadOnly,
#     ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDestroyAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

