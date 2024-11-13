from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.models import Categories,Post,Comment,UserProfile
from .serializers import CategoriesSerializer,PostSerializer,CommentSerializer,UserProfileSerializer
from rest_framework.permissions import AllowAny


class UserProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    

class CategoriesListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]

class CategoriesCreateView(generics.CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CategoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    
    def perform_create(self, serializer):
        # Oturum açmış bir kullanıcı varsa onun profilini kullan
        if self.request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=self.request.user)
            serializer.save(post_user=user_profile)
                

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
