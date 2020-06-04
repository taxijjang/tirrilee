from django.shortcuts import render,redirect

from .forms import PostsForm, PostSearchForm
from .models import Posts
from users.models import Users

from django.db.models import Q

def home(request):
    posts = Posts.objects.all()
    print("home posts")
    print(posts)
    return render(request,'home.html', {'posts':posts})

def post_write(request):
    if not request.session.get('user'):
        return redirect('/users/login')

    if request.method == "GET":
        form = PostsForm()
        return render(request, 'post_write.html', {'form': form})

    elif request.method == "POST":
        form = PostsForm(request.POST, request.FILES)

        if form.is_valid():
            print("post valid")
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_post = form.save(commit=False)
            new_post.writer = user
            new_post.save()
            return redirect('home')

        return render(request, 'post_write.html', {'form': form})

def post_search(request):
    if request.method == "GET":
        form = PostSearchForm()
        return render(request, 'post_search.html',{'form':form})

    elif request.method == "POST":
        form = PostSearchForm(request.POST)

        if form.is_valid():
            search_word = form.cleaned_data['product']
            search_weather = form.cleaned_data['classification']

            post_list = Posts.objects.filter(Q(product__icontains=search_word) &
                                             Q(classification__icontains=search_weather))
            print("post_search")
            print(post_list)

            form = PostSearchForm()
            return render(request, 'post_search.html',{'post_list': post_list, 'form' : form})

    return render(request,'post_search.html')


