from django import forms
from .models import Category , ZirCategory , Tags , Product , Color , Size , GalleryImage , Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ZirCategoryForm(forms.ModelForm):
    class Meta:
        model = ZirCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'
        widgets = {
            'tag_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'tozihat' : forms.TextInput(attrs={'class': 'form-control'}),
            'alt' : forms.TextInput(attrs={'class': 'form-control'}),
            'alt_2' : forms.TextInput(attrs={'class': 'form-control'}),
            'size_asli' : forms.TextInput(attrs={'class': 'form-control'}),
            'price_asli' : forms.NumberInput(attrs={'class': 'form-control'}),
            'tedad_mahsol' : forms.NumberInput(attrs={'class': 'form-control'}),
            'takhfif' : forms.NumberInput(attrs={'class': 'form-control','max':100,'min':0}),
            'zir_category': forms.Select(attrs={'required': 'required'}),
        }

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'Ekhtelaf': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        widgets = {
            'Ekhtelaf': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = '__all__'
        widgets = {
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['product','username','title','body','parent']

class CommentFormCMS(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'product' : forms.Select(attrs={'class': 'form-control'}),
            'parent' : forms.Select(attrs={'class': 'form-control'}),
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'like' : forms.NumberInput(attrs={'class': 'form-control'}),
            'created' : forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
