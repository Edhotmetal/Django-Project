from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,
                                CreateView, UpdateView, DeleteView)
from django.core.exceptions import PermissionDenied

# Create your views here.

class DefaultContextMixin():
    def get_context(self, ):
        if self.context:
            context = self.context
            context['current_user'] = self.request.user
            return context
        else:
            return ["DEFAULT CONTEXT"]

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(DefaultContextMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostMixin(object,):
    def form_valid(self, form, ):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreatePostView(CreatePostMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

# Make sure the user is the author of the current post before editing
# https://stackoverflow.com/questions/55510300/how-to-protect-user-from-editing-others-blog-posts-in-django
class IsAuthorMixin(object):
    permission_denied_message = ("You are not the author of this post - you cannot edit it")

    def dispatch (self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            raise PermissionDenied(self.get_permission_denied_message())
        return super().dispatch(request, *args, **kwargs)

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        return self.permission_denied_message

class PostUpdateView(IsAuthorMixin, LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostDeleteView(IsAuthorMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True,
                author=get_object_or_404(User,username=self.request.user).id).order_by('create_date')

###########################
###########################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)
