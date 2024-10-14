

from django import forms

from . models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item # Links the form to the Item model
        fields=['item_name','item_price','item_desc','item_image']