from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CommentForm, SearchForm
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts1'
    paginate_by = 2
    queryset = Post.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['liked_posts'] = Post.objects.filter(likes__gt=0).order_by('-likes')
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(title__icontains=search_text)
            | Q(text__icontains=search_text)

        )
        return q


# #               0        1      2
# created_at= ['12:30','12:36','12:54']
# #             -3        -2      -1
# name = 'Vlad'
# name = 'Jhon'
# name = 'Vlad'
# print(name)
# name = 'Mike'
# print(name)

from .forms import CommentForm
class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm()
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))



from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
class LikePostView(View,LoginRequiredMixin):
    def post(self,request,pk,*args,**kwargs):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
            return redirect('post_detail', pk=post.pk)

