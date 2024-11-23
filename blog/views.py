from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-data_creation')

        if self.request.GET.get('search'):
            queryset = queryset.filter(title__icontains=self.request.GET.get('search'))

        return queryset


@method_decorator(login_required(login_url='accounts/login'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        current_user = User.objects.get(username=self.request.user)
        form.instance.author = current_user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


@method_decorator(login_required(login_url='accounts/login'), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostForm
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='accounts/login'), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/'
    