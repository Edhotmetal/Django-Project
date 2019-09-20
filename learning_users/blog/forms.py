from django import forms
from blog.models import Post, Comment
from basic_app.models import UserProfileInfo

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        labels = {
                'author':''
                }

        widgets = {
                'author':forms.TextInput(attrs={'hidden':''}),
                'title':forms.TextInput(attrs={'class':'textinputclass'}),
                'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
                }
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
                'author':forms.TextInput(attrs={'class':'textinputclass'}),
                'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
                }
