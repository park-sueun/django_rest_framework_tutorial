from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# 별도의 검색엔진을 사용하는 것이 아니라, DBMS의 where절을 사용
from rest_framework.filters import SearchFilter, OrderingFilter

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
    
    # permission_classes = [IsAuthenticated] # permission이 적용됨
    
    filter_backends = [SearchFilter]
    search_fields = ['message']     # ?search= -> QuerySet 조건 절에 추가할 필드 지정. 모델 필드 중 문자열 필드만을 지정
    
    def perform_create(self, serializer):
        # FIXME: 유저 인증이 되어 있다는 가정하에 auth를 지정함
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)
    
    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)