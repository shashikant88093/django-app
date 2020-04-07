from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

# HyperlinkedIdentityField,

from posts.models import Post
from accounts.api.serializers import UserDetailSerializer

class PostDetailSerializer(ModelSerializer):
    class Meta:
        user = UserDetailSerializer(read_only = True)
        model = Post
        fields = [
            'user',
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish'
        ]


class PostListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only = True)
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='slug'
    )
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'id',
            'title',
            # 'slug',
            'content',
            'delete_url'
        ]
    def get_user(self,obj):
        return str(obj.user.username)