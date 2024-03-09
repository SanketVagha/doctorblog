# forms.py
from django import forms
from .models import Blog

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
