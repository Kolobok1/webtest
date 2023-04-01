from .models import Articles
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        
        model = Articles
        fields = ('title', 'question', 'answer','option')
        widgets = {
            'title': Textarea(attrs={'placeholder': 'Название теста','cols': 60, 'rows': 2}),
            'question': Textarea(attrs={'placeholder': 'Вопрос','cols': 40, 'rows': 1}),
            'answer': Textarea(attrs={'placeholder': 'Ответ','cols': 20, 'rows': 1}),
            'option': Textarea(attrs={'placeholder': 'Вариант','cols': 20, 'rows': 1}),
        }
        
        
        # model = Articles
        # fields = ('title', 'question', 'answer')
        # widgets = {
        #     'title': TextInput(attrs={
        #         'cols': 20,
        #         'rows': 50,
        #         'placeholder': 'Название теста'}),
        # }



