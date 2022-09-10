from django import forms

from .models import Movie


class PostMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title', 'description'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add movie title here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add movie description here'}),
        }


class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title', 'description'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
