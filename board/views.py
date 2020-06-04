from django.shortcuts import render,redirect

from .forms import PostsForm
from .models import Posts
from users.models import Users

def home(request):
    posts = Posts.objects.all()
    return render(request,'home.html', {'posts':posts})

def post_write(request):
    if not request.session.get('user'):
        return redirect('/users/login')

    if request.method == "GET":
        form = PostsForm()
        return render(request, 'post_write.html', {'form': form})

    elif request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        print(request.POST.get('product'))
        print(request.POST.get('price'))
        print(request.POST.get('classification'))
        print(request.POST.get('product_image'))

        if form.is_valid():
            print("post valid")
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_post = form.save(commit=False)
            new_post.writer = user
            new_post.save()
            return redirect('home')

        print("post not valid")
        return render(request, 'post_write.html', {'form': form})
