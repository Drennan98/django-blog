from about.models import CollaborateRequest
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')