from django import forms
from blog.models import Post, Comment
from basic_app.models import UserProfileInfo
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        text = forms.CharField(widget=TinyMCE(attrs={'class':'editable textarea postcontent'})),
        fields = ('title','text')
        author = forms.TextInput(attrs={'hidden':''}),
        title = forms.TextInput(attrs={'class':'textinputclass'}),

        labels = {
                'author':''
                }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
                'author':forms.TextInput(attrs={'class':'textinputclass'}),
                'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
                }
