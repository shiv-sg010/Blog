from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Sub_Post


class SubPostDetailView(DetailView):
    model = Sub_Post
    template_name= 'sub_blog/sub_post_detail.html'


class SubPostCreateView(LoginRequiredMixin, CreateView):
    model = Sub_Post
    template_name='sub_blog/sub_post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SubPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sub_Post
    template_name='sub_blog/sub_post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SubPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sub_Post
    template_name='sub_blog/sub_post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
