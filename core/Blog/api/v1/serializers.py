from rest_framework import serializers
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Post
        fields = ('id', 'title' , 'author' , 'content' , 'status' , 'created_time' , 'updated_time' , 'published_time' , 'category')