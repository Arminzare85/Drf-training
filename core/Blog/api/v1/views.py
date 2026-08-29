from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from .serializers import PostSerializer , CategorySerializer
from ...models import Post , Category
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


# Create your views here.
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT' , 'DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request , id):
#     post = Post.objects.get(id=id)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response("Post deleted" , status=204)







""" CBV to showing posts """
# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class PostDetail(RetrieveUpdateDestroyAPIView ):

#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
        


""" CBV to CRUD posts in one view """
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter]
    filterset_fields = ['category','author']
    search_fields = ['title' , 'content']

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer