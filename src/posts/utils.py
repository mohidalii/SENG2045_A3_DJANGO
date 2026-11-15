from .models import Post
from profiles.models import Profile
from django.http import HttpResponse
from django.shortcuts import redirect

def action_permission(func):
    def wrapper(request, **kwargs):
        pk = kwargs.get('pk')
        profile = Profile.objects.get(user=request.user)
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return redirect('posts:main-board')
        if profile.user == post.author.user:
            print('yes')
            return func(request, **kwargs)
        else:
            print('no')
            # return HttpResponse('access denied - you need to be the author of this post to delete.')
            return redirect('posts:main-board')

    return wrapper