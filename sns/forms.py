from django import forms
from.models import Message,Good
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class":"from-control","rows":2})
        }

# class PostForm(forms.Form):
#     content = forms.CharField(max_length=500,\
#         widget=forms.Textarea(attrs={'class':'from-control','rows':2}))

#     def __init__(self, user,*args, **kwards):
#         super(PostForm,self).__init__(*args, **kwards)