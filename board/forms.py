from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["product","price",'classification','product_image']
        widgets = {
             'product': forms.TextInput(attrs={'class': 'input_info', 'placeholder': "상품명을 입력해주세요."}),
             'price': forms.NumberInput(attrs={'class': 'input_info', 'placeholder': "상품 가격을 입력해주세요."}),
             'classification': forms.CheckboxSelectMultiple(),
             #'product_image': forms.FileInput(),
        }
        labels = {
            'product': '상품명',
            'price': '가격',
            'classification': '분류',
            'product_image': '사진첨부',
        }