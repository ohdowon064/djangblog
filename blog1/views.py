from django.shortcuts import render
from .models import Post

def post_list(request):
    post_qs = Post.objects.all()
    return render(request, 'blog1/post_list.html', {'post_list': post_qs})
