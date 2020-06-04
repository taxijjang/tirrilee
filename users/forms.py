from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["email","password","nickname","cellphone"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input_info', 'placeholder': "이메일을 입력해주세요."}),
            'password': forms.PasswordInput(attrs= {'class': 'input_info', 'placeholder': "숫자,영문,특수문자 포함 12자."}),
            'nickname': forms.TextInput(attrs={'class': 'input_info', 'placeholder': "사용할 닉네임을 입력해주세요."}),
            'cellphone': forms.TextInput(attrs={'class': 'input_info', 'placeholder': " '-' 제외 숫자만 입력해주세요."}),
        }
        labels = {
            'email': '이메일',
            'password': '비밀번호',
            'nickname': '닉네임',
            'cellphone': '연락처',
        }

class UsersInsertForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['image']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["email","password"]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input_info', 'placeholder': "이메일을 입력해주세요."}),
            'password': forms.PasswordInput(attrs={'class': 'input_info', 'placeholder': "숫자,영문,특수문자 포함 12자."}),
        }
        labels = {
            'email': '',
            'password': '',
        }
