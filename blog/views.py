from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    posts = Post.objects.order_by('pub_date')
    context = {'posts': posts}
    return render(request,'blog/index.html',context)

def detail(request,pk):
    post_info = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/detail.html',{'detail':post_info})

def post(request,pk):
    post_detail = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post.html',{'post':post_detail})
