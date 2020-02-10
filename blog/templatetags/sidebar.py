from django import template

register = template.Library()


@register.inclusion_tag("sidebar.html")
def show_sidebar(Post):
    posts = Post.choice_set.all()
    return {"posts": posts}
