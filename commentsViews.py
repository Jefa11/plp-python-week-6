# comments/views.py
from django.shortcuts import redirect
from .models import Comment
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@require_POST
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Comment.objects.create(
        post=post,
        author=request.user,
        content=request.POST['content']
    )
    return redirect('post_detail', pk=post_id)
