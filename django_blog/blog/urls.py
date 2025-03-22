from django.urls import path
from .views import  (RegisterView, ProfileView, LoginView, LogoutView,
                      BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostEditView,
                      BlogPostDeleteView
                      )

urlpatterns = [

    #Authentication URLs
    path('register/', RegisterView, name="register"),
    path('login/', LoginView, name="login"),
    path('logout/', LogoutView, name="logout"),
    path('profile/', ProfileView, name="profile"),

    #Blog Post URLs
    path('posts/', BlogPostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="post-detail"),
    path("posts/new", BlogPostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", BlogPostEditView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete", BlogPostDeleteView.as_view(), name="post-delete"),
]