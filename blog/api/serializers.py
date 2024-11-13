from rest_framework import serializers
from blog.models import Categories,Post,Comment,UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['foto']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    post_user = serializers.StringRelatedField(read_only=True)
    Categories = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'