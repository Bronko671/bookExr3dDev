from django import forms
from django.forms import ModelForm
from .models import Book, Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = {
            'name',
            'web',
            'price',
            'picture'
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = {
            'name', 
            'email',
            'body'
        }


class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))