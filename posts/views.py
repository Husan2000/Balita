from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Post, Comment, Tag, Category
from .forms import CreateCommentForm
from django.urls import reverse


def home_view(request):
    posts = Post.objects.order_by('id')[:3]
    articles = Post.objects.order_by('-id')[:3]
    blogs = Post.objects.order_by('-id')[:8]
    context = {
        'object_list': posts,
        'object_list1': articles,
        'object_list2': blogs
    }
    return render(request, 'posts/index.html', context)


def post_detail_view(request, slug):
    form = CreateCommentForm()
    post = get_object_or_404(Post, slug=slug)
    last_3_posts = Post.objects.order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post__slug=slug).order_by('-id')

    if request.method == 'POST':
        form = CreateCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'/detail/{post.slug}#comments')
    context = {
        'object': post,
        'last_3_posts': last_3_posts,
        'categories': categories,
        'tags': tags,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/detail.html', context)
