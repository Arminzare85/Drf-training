from django.shortcuts import render
from django.views.generic import TemplateView , RedirectView , ListView
from .models import Post



# Create your views here.
class PostView(TemplateView):
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context


class GoToGoogleView(RedirectView):
    url = 'https://www.google.com'


class PostDetailView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
