from django import forms
from .models import Article
from ckeditor.fields import RichTextField

class CreateArticle(forms.ModelForm):
  body =RichTextField()
  class Meta:
    model = Article
    fields = ["title", "body", "thumb", "status"]




  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['title'].widget.attrs.update({'class':'form-control','Placeholder': 'Title here.'})
      #self.fields['body'].widget.attrs.update({'class':'form-control','Placeholder': 'Enter your blog here.'})
      self.fields['status'].widget.attrs.update({'class':'form-control','class':'form-select'})
      self.fields['thumb'].widget.attrs['class'] = 'form-control'


class UpdateArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ["title", "body", "thumb", "status"]