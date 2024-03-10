from django import forms
from CRUDOpsByDjango.models import UserModel
from CRUDOpsByDjango.models import ProductDetailsModel
class Userforms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class Productforms(forms.ModelForm):
    class Meta:
        model = ProductDetailsModel
        fields = "__all__"