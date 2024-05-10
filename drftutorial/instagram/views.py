from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PublicPostListViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# TODO: APIView로 만들어보기!
class PostView(APIView):
    def get(self, request):
        pass