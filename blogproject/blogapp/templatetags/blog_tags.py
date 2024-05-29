from blogapp.models import Post
from django import template
from django.db.models import Count

register=template.Library()
@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blogapp/latest_posts.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:6]
    return {'latest_posts':latest_posts}

@register.simple_tag()
def get_post_commented_posts(count=3):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]