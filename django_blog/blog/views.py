from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment
from taggit.models import Tag
from django.db.models import Q
from .forms import CommentForm

    #Blog post Detail, update, delete views

class BlogPostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['author', 'title', 'content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        # Redirect to the list of blog posts after successful creation
        return reverse_lazy('post-list')
  


class BlogPostListView(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_form.html'

class BlogPostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

class BlogPostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/edit.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-form')


    # Register view

def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created successfully 🐊")
            return redirect('login')#......................................................
        else:
            messages.error(request, "Error please try again!")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {'form': form})


    #login view

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, " 🫎 welcome to the home page  🫎")
            return redirect('profile')

        else:
            messages.error(request, "error please login with correct email or password")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {'form': form})


    #profile view

def ProfileView(request):
    return render(request, 'blog/profile.html')

    #logout view

def LogoutView(request):
    logout(request)
    return redirect('login')





    # comments section


# Create Comment View (for adding new comments)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        # Set the post and author when the form is valid
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})


# Update Comment View (for editing existing comments)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})


# Delete Comment View (for deleting comments)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    context_object_name = 'comment'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})
    




     #View to display posts filtered by a tag
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']  # Capture the tag_slug from the URL
        tag = Tag.objects.get(slug=tag_slug)  # Get the tag object
        return Post.objects.filter(tags=tag)  # Filter posts by this tag
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        if tag:
            return Post.objects.filter(tags__name=tag)
        return super().get_queryset()


def search_view(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})

