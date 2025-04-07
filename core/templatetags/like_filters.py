from django import template
from core.models import LikePost

register = template.Library()


@register.filter
def user_has_liked(post, user):
    if not user.is_authenticated:
        return False
    
    return LikePost.objects.filter(post_id=post.id, username=user.username).exists()
