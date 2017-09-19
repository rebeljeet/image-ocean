from posts.models import Post


def get_posts():

    posts = Post.objects.order_by('-date_created')

    return posts


def get_post(slug=None):
    if not slug:
        return None

    post = Post.objects.get(slug=slug)

    return post
