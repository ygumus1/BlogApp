from django.urls import path
from .views import CategoriesCreateView,CategoriesDetailView,PostListView,PostCreateView,PostDetailView,CommentCreateView,CommentListView,UserProfileList,CategoriesListView,UserProfileCreateView

urlpatterns =[
    path('UserProfiles/',UserProfileList.as_view(),name='user-profile-list'),
    path('UserProfileCreate/',UserProfileCreateView.as_view(),name='user-profile-create'),
    path('Categories/',CategoriesListView.as_view(),name ='categories-list'),
    path('CategoriesCreate/',CategoriesCreateView.as_view(),name='categories-create'),
    path('Categories/<int:pk>/',CategoriesDetailView.as_view(),name='categories-detail'),
    path('Posts/',PostListView.as_view(),name='post-list'),
    path('PostCreate/',PostCreateView.as_view(),name='post-create'),
    path('Posts/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('Comments/',CommentCreateView.as_view(),name='comment-list'),
    path('Comments/<int:pk>/',CommentListView.as_view(),name='comment-detail'),

    
]