# -*- encoding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from board.views import list_posts, show_post_detail, PostCreateView, CommentCreateView


# 条件によってルーティングを切り替える
def dispatch_by_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        view = CommentCreateView.as_view()
    else:
        view = show_post_detail
    return view(request, *args, **kwargs)


urlpatterns = patterns('',
   url(r'^$', list_posts, name='home'),
   url(r'^add$', login_required(PostCreateView.as_view()), name='add_new_post'),
   url(r'^(?P<pk>\d+)$', dispatch_by_login, name='show_post_detail'),
)
