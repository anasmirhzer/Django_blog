"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import BlogPostListPosts, BlogPostDetailPost, BlogPostAddPost, BlogPostUpdatePost, BlogPostDeletePost
from djangoBlog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogPostListPosts.as_view(), name='home'),
    path('<str:slug>', BlogPostDetailPost.as_view(), name='post_details'),
    path('CreatePost/', BlogPostAddPost.as_view(), name='add_post'),
    path('<str:slug>/UpdatePost', BlogPostUpdatePost.as_view(), name='edit_post'),
    path('<str:slug>/DeletePost', BlogPostDeletePost.as_view(), name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
