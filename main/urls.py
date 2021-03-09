from django.contrib import admin
from django.urls import path
from .views import (PostListView,
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )
from . import views


urlpatterns = [
    path('', views.home, name='hotel-home'), 
    path('about/', views.about, name="hotel-about"), 
    path('blog/', PostListView.as_view(), name="hotel-blog"), 
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"), 
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),  
    path('post/new/', PostCreateView.as_view(), name="post-create"), 
    path('user/<str:username>',UserPostListView.as_view(),name="user-posts"),

]