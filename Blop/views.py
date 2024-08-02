from django.shortcuts import render
from .models import Post

def blop(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
    return render(request, "Blop/blop.html", {'posts':posts})
