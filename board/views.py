# -*- encoding: utf8 -*-
import os
import random
import string

from django.conf import settings
from django.shortcuts import render
from django.views.generic.edit import CreateView

from board.models import Post, Comment
from board.forms import PostForm, CommentForm


def list_posts(request):
    return render(request, 'board/list_posts.html', {'posts': Post.objects.order_by('updated_at').reverse().all()})


def show_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})


# class based generic view sample
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        # 一覧にリダイレクトする
        return reverse('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        # 一覧にリダイレクトする
        return reverse('show_post_detail', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super(CommentCreateView, self).form_valid(form)
