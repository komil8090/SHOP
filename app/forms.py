from django import forms
from .models import Product,Order,Comment

# forms.Form
# forms.ModelForm



class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()
   

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'category']
        
        
class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('product',)




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name...'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'rows': 4
            })
        }
