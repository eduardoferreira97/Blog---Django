from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .post import PostForm


def index(request):
    posts = Post.objects.order_by('pub_date')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post_info = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'detail': post_info})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {'form': form})
