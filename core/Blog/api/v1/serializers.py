from rest_framework import serializers
from ...models import Post , Category 
from accounts.models import Profile
from django.urls import reverse


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), many=False)
    snippet = serializers.CharField(max_length=255, read_only=True)
    absolute_url = serializers.SerializerMethodField()
    image = serializers.ImageField( required=False)

    class Meta:
        model = Post
        fields = ('id', 'title' , 'author' , 'content' , 'status','absolute_url', 'created_time','snippet' , 'updated_time' , 'published_time' , 'category' , 'image' , 'category')
        read_only_fields = ('author','snippet')
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(
            f'/blog/api/v1/post/{obj.pk}/'
        )
    
    def to_representation(self, instance):
        request = self.context.get('request')
        ret = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk') :
            ret.pop('snippet', None)
            ret.pop('absolute_url', None)
        else:
            ret.pop('content', None)
            
        ret['category'] =CategorySerializer(instance.category).data
        return ret

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context['request'].user.id)

        return super().create(validated_data)