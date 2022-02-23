from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)

    # instangram/templates/instangram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def archive_year(request, year):
    return f"{year}년 archives."
