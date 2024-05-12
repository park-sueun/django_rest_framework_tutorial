from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer

# Create your views here.
    
# class PublicPostListView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
        
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(
#                 serializer.data, 
#                 status=status.HTTP_201_CREATED
#             )
            
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )


# class PostView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Post, pk=pk)
    
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# APIView -> mixins -> GenericAPIView -> ViewSet
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer