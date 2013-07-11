from django.contrib import admin
from board.models import Post, Comment


class PollAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'shorten_body', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_filter = ['created_at', 'updated_at']

    def shorten_body(self, model):
        if len(model.body) > 100:
            return model.body[:100] + '...'
        else:
            return model.body


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'shorten_body', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_filter = ['created_at', 'updated_at']

    def post_subject(self, model):
        return model.post.subject

    def shorten_body(self, model):
        if len(model.body) > 100:
            return model.body[:100] + '...'
        else:
            return model.body


admin.site.register(Post, PollAdmin)
admin.site.register(Comment, CommentAdmin)
