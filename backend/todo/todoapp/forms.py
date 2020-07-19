from django import forms
from datetime import datetime


class TodoForm(forms.Form):
    due_date = forms.DateTimeField(required=False)

    title = forms.CharField(
        required=True,
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your title',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        )
    )

    text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your text',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        )
    )