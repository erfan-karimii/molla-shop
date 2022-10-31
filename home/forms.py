from django import forms
from .models import FooterAsli ,FooterZir , NavOne , NavTwo , NavThree ,SiteSetting , Slider , Tabligh,TagFooter,TagNav , TagNewPage , ZirSlider
from product.models import Tags

class FooterAsliForm(forms.Form):
    name = forms.CharField(max_length=100)

class FooterZirForm(forms.Form):
    footer = forms.ModelChoiceField(queryset=FooterAsli.objects.all())
    name = forms.CharField(max_length=50)
    link = forms.CharField(max_length=100)

class FooterZirUpdateForm(forms.ModelForm):
    class Meta:
        model = FooterZir
        fields = '__all__'

class NavOneForm(forms.ModelForm):
    class Meta:
        model = NavOne
        fields = '__all__'

class NavTwoForm(forms.ModelForm):
    class Meta:
        model = NavTwo
        fields = '__all__'

class NavThreeForm(forms.ModelForm):
    class Meta:
        model = NavThree
        fields = '__all__'
        widgets = {
            'url_title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'})
        }

class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields ="__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
            'alt2': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'text_products_view': forms.TextInput(attrs={'class': 'form-control'}),
            'link_products_view' : forms.TextInput(attrs={'class': 'form-control'}),
            'footer_text' : forms.TextInput(attrs={'class': 'form-control'}),
            'alt_bg': forms.TextInput(attrs={'class': 'form-control'}),
            'telephon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = "__all__"
        widgets = {
            'text1': forms.TextInput(attrs={'class': 'form-control'}),
            'text2': forms.TextInput(attrs={'class': 'form-control'}),
            'text3': forms.TextInput(attrs={'class': 'form-control'}),
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
            'name_button': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }        

class TablighForm(forms.ModelForm):
    class Meta:
        model = Tabligh
        fields = '__all__'
        widgets = {
            'name_button': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class tag_footer_forms(forms.ModelForm):
    class Meta:
        model = TagFooter
        fields ="__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Tag_navbr_form(forms.ModelForm):
    class Meta:
        model = TagNav
        fields =['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TagNewPageForm(forms.ModelForm):
    class Meta:
        model = TagNewPage
        fields ="__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ZirSliderForm(forms.ModelForm):
    class Meta:
        model = ZirSlider
        fields ="__all__"
        widgets = {
            'text1' : forms.TextInput(attrs={'class': 'form-control'}),
            'name_button1' : forms.TextInput(attrs={'class': 'form-control'}),
            'link1' : forms.TextInput(attrs={'class': 'form-control'}),
            'text2' : forms.TextInput(attrs={'class': 'form-control'}),
            'name_button2' : forms.TextInput(attrs={'class': 'form-control'}),
            'link2' : forms.TextInput(attrs={'class': 'form-control'}),
            'text3' : forms.TextInput(attrs={'class': 'form-control'}),
            'name_button3' : forms.TextInput(attrs={'class': 'form-control'}),
            'link3' : forms.TextInput(attrs={'class': 'form-control'}),
            'text4' : forms.TextInput(attrs={'class': 'form-control'}),
            'name_button4' : forms.TextInput(attrs={'class': 'form-control'}),
            'link4' : forms.TextInput(attrs={'class': 'form-control'}),
        }

