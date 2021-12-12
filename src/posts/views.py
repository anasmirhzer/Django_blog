from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

# Create your views here.
from posts.models import BlogPost
from posts.forms import BlogPostForm


class BlogPostListPosts(ListView):
    model = BlogPost
    template_name = 'posts/home.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostDetailPost(DetailView):
    model = BlogPost
    template_name = 'posts/post.html'
    context_object_name = 'post'


class BlogPostAddPost(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()

        if self.request.user.is_authenticated:
            initial['author'] = self.request.user
        initial['created_on'] = datetime.today()
        initial['published'] = True
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Create post'
        return context


class BlogPostUpdatePost(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Update post'
        return context


class BlogPostDeletePost(DeleteView):
    model = BlogPost
    template_name = 'posts/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')
    