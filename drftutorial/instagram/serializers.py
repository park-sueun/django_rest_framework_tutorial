from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username"]
        
class PostSerializer(serializers.ModelSerializer):
    # # 외래키로 지정된 필드의 값을 가져오는 방법 1
    # username = serializers.ReadOnlyField(source='author.username')
    
    # class Meta:
    #     model = Post
    #     fields = ("pk", "username", "message", "updated")
    
    # 외래키로 지정된 필드의 값을 가져오는 방법 2
    author = AuthorSerializer()
    
    class Meta:
        model = Post
        fields = "__all__"