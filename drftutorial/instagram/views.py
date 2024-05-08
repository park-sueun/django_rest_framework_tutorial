from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PublicPostListViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    