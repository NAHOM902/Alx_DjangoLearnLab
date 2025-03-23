from django.urls import path
from .views import  (RegisterView, ProfileView, LoginView, LogoutView,
                      BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostEditView,
                      BlogPostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView
                      )

urlpatterns = [

    #Authentication URLs
    path('register/', RegisterView, name="register"),
    path('login/', LoginView, name="login"),
    path('logout/', LogoutView, name="logout"),
    path('profile/', ProfileView, name="profile"),

    #Blog Post URLs
    path('post/', BlogPostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="post-detail"),
    path("post/new/", BlogPostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", BlogPostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="post-delete"),


    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]