from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog_app/home.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog_app/post_detail.html", {"post": post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog_app/post_create.html", {"form": form})
