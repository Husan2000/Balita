from django.shortcuts import render
from about.models import About, LatestPosts


def about_view(request):
    users = About.objects.all()
    posts = LatestPosts.objects.all()
    populars = LatestPosts.objects.order_by('-id')[:3]
    context = {
        'users': users,
        'posts': posts,
        'populars': populars,
    }
    return render(request, 'about/index.html', context)
