from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post






class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']




from taggit.forms import TagWidget  # Import TagWidget if using django-taggit for tags

# Post creation and update form with custom widgets
class PostForm(forms.ModelForm):
    # Custom widget for the 'tags' field, if using django-taggit
    tags = forms.CharField(
        widget=TagWidget(),  # Uses the TagWidget for tag input
        required=False
    )
    
    # You can also customize other fields if necessary
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))  # Custom textarea widget

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in the form fields

class CustomTextWidget(forms.Textarea):
    def __init__(self, attrs=None):
        # You can add custom attributes for the widget here
        if attrs is None:
            attrs = {}
        attrs.update({'class': 'custom-text-widget', 'placeholder': 'Enter text here...'})
        super().__init__(attrs)