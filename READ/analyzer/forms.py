from django import forms
from .models import User_Image

class ImageForm(forms.ModelForm):
    cover = forms.ImageField(
        error_messages={
            'required':'이미지를 업로드해주세요.'
        },
        label='이미지'
    )
 
    class Meta:
        model = User_Image
        fields = ['cover']