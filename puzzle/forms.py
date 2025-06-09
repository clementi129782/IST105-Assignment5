from django import forms

class PuzzleForm(forms.Form):
    number = forms.IntegerField(label='Enter a number', required=True)
    message = forms.CharField(label='Enter a message', max_length=100, required=True)