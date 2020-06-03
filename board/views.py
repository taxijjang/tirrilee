from django.shortcuts import render,redirect

from .forms import PostsForm
from .models import Posts
from users.models import Users

def home(request):
    return render(request,'home.html')

def post_write(request):
    if not request.session.get('user'):
        return redirect('/users/login')

    if request.method == "GET":
        form = PostsForm()

    elif request.method == "POST":
        form = PostsForm(request.POST)
        print(form)

        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_post = Posts(
                product = form.cleaned_data['product'],
                price = form.cleaned_data['price'],
                classification = form.cleaned_data['classification'],
                writer = user
            )
            new_post.save()
            return redirect('home')
    return render(request,'post_write.html', {'form':form})