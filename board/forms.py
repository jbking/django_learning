from board.models import Post, Comment
from django.forms import ModelForm, FileField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'body', 'icon')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
