from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from ...models import Post
from rest_framework.views import APIView

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
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




class PostDetail(APIView):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    def put(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, id):
        post = Post.objects.get(id=id)
        post.delete()
        return Response("Post deleted" , status=204)
        
