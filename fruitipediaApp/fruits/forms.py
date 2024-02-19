from django import forms

# Here we create user forms to handle the user input
from fruitipediaApp.fruits.models import Fruit





class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitCreateForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitEditForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        pass


class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']
