from django import forms

from .models import Movie


class PostMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title', 'description', 'user'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add movie title here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add movie description here'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title', 'description'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
