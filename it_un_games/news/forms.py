from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'city', 'tags', 'desc', 'price']

        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название игры'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            "tags": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Теги'
            }),
            "desc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание игры'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
        }