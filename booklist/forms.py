from django import forms
from django.forms import fields, widgets, ModelForm
from .models import Book
from django.forms.widgets import DateInput



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'datepublished','numpages','booktype']
        labels = {
            'title' : 'Title',
            'author' : 'Author',
            'datepublished' : 'Date Published',
            'numpages' : 'Number of Pages',
            'booktype' : 'Type'
        }

        widgets = {
            'datepublished' : DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        super(BookForm,self).__init__(*args, **kwargs)
        self.fields['booktype'].empty_label = "Select"
        self.fields['datepublished'].required = False
        self.fields['numpages'].required = False
        self.fields['booktype'].required = False
        