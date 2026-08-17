from django.shortcuts import render
from django.views.generic import TemplateView , RedirectView , ListView , DetailView , FormView , CreateView
from django.core.paginator import Paginator
from .forms import PostForm
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


class PostListView(ListView , Paginator):
    model = Post
    context_object_name = 'posts'
    paginate_by = 4
    ordering = ['-author']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"
    
# class CreatePostView(FormView):
#     template_name = 'create.html'
#     form_class = PostForm
#     success_url = '/blog/post/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class CreatePostView(CreateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    success_url = '/blog/post/'
