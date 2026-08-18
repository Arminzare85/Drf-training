from django.shortcuts import render
from django.views.generic import TemplateView , RedirectView , ListView , DetailView , UpdateView , CreateView , DeleteView
from django.core.paginator import Paginator
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin


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

class CreatePostView(PermissionRequiredMixin , LoginRequiredMixin , CreateView):
    permission_required = "blog.add_post"
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    success_url = '/blog/post/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()



class PostEditView(PermissionRequiredMixin , LoginRequiredMixin , UpdateView):
    permission_required = "blog.edit_post"
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    template_name = 'create.html'



class PostDeleteView(PermissionRequiredMixin , LoginRequiredMixin  , DeleteView):
    permission_required = "blog.delete_post"
    model = Post
    success_url = '/blog/post/'
