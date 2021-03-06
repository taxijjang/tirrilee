from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Users
from .forms import UsersForm, UsersInsertForm,LoginForm

#-- 회원가입
def register(request):
    if request.method == "GET":
        form = UsersForm()
        return render(request, 'register.html', {'form': form})

    elif request.method == "POST":
        form = UsersForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = Users(
                email = form.cleaned_data['email'],
                password = make_password(form.cleaned_data['password']),
                nickname = form.cleaned_data['nickname'],
                cellphone = form.cleaned_data['cellphone']
            )
            new_user.save()
            print(new_user)
            return redirect('home')
        else:
            print("register valid error")
            return render(request,'register.html', {'form':form})



#-- 로그인
def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    elif request.method == "POST":
        print("login POST 진입")
        form = LoginForm(request.POST)
        errorMsg = {}

        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

        try:
            print('try 진입')
            user = Users.objects.get(email=email)
            print(user)
            if check_password(password,user.password):
                print("비밀번호 일치")
                request.session['user'] = user.id
                return redirect('home')
            else:
                print("비밀번호 불일치")
                errorMsg['error'] = "아이디 또는 비밀번호가 다릅니다."

        except Users.DoesNotExist:
            print("except 진입")
            errorMsg['error'] = "아이디가 없습니다"

        print("끝")
        form = LoginForm()
        return render(request, 'login.html', {'form': form} )


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('home')

def profile(request, id):
    user_id = request.session.get('user')
    user = Users.objects.get(pk=user_id)
    print(user)
    return render(request,'profile.html', {'user':user})

def insert(request, id):
    print("insert 진입")
    if not request.session.get('user'):
        return redirect('login')

    if request.method == "GET":
        user = Users.objects.get(pk=id)
        form = UsersInsertForm(instance=user)
        return render(request,'insert.html',{'form':form,'user':user})

    elif request.method == "POST":
        user = Users.objects.get(pk=id)
        form = UsersInsertForm(request.POST, request.FILES, instance= user)
        print(request.POST.get('image'))
        if form.is_valid():
            form.save()
            return redirect('/users/profile/' + str(user.id))