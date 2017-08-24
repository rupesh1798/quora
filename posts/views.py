from django.shortcuts import render, get_object_or_404
from .models import Post, Answer

def post_list(request):
    posts = Post.objects.order_by('published_date')
    answers = Answer.objects.order_by('upvotes')
    return render(request, 'posts/home.html', {'posts': posts, 'answers':answers})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    answers = Answer.objects.filter(question = post).order_by('date')
    return render(request, 'posts/post_detail.html', {'post': post, 'answers':answers})
