from django import forms
from blogapp.models import Comments

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.CharField()
    comments=forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')