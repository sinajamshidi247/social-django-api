from django import forms 
from . models import Post, Comment



class AddPostForm(forms.ModelForm):
    class Meta:

        model=Post
        fields=('body',)


class EditPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('body',)


class AddPostForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)


        widgets={
            'body':forms.Textarea(attrs={'placeholder':'your comment'})

        }

        error_messages={
            'body':{
                'required':'fill this field :/'
            }
        }


class AddReplyForm(forms.ModelForm):
      class Meta:
        model=Comment
        fields=('body',)
