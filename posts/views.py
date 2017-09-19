from __future__ import absolute_import

from django.views import generic

from .models import Post
from .forms import CreatePostForm
from .helpers import get_post


class DetailPostView(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(DetailPostView, self).get_context_data(**kwargs)
        context['post'] = get_post(self.kwargs['slug'])

        return context


class CreatePostView(generic.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return super(CreatePostView, self).form_valid(form)
