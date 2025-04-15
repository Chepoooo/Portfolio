from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post

def blogMain(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request,'posts.html',context)


def post_detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'post_detail.html', {'post':post})

    