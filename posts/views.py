from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()

    context= {
        'posts' : posts,
        'comment_form' : comment_form,
    }

    return render(request,'index.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    
    else: 
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)
@login_required
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)

        # 현재 로그인 유저
        comment.user = request.user
        # post_id를 기준으로 찾은 post
        post = Post.objects.get(id=post_id)
        comment.post = post

        comment.save()

        return redirect('posts:index')
    
@login_required

def like(request, post_id):




    # 좋아요 버튼을 누른 유저

    user = request.user

    post = Post.objects.get(id=post_id)




    # 이미 좋아요 버튼을 누른경우

    # if user in post.like_users.all():

    if user in post.like_users.all():

        post.like_users.remove(user)

        # user.like_posts.remove(post)




    # 좋아요 버튼을 아직 안누른경우

    else:

        post.like_users.add(user)

        # user.like_posts.add(post)




    return redirect('posts:index')


