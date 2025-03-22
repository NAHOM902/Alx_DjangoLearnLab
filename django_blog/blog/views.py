from django.shortcuts import render, redirect
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
    template_name = 'blog/Post_confirm_delete.html'
    success_url = reverse_lazy('post-list')


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