from django import forms
from .models import TopProductSelection

class TopProductSelectionForm(forms.ModelForm):
    class Meta:
        model = TopProductSelection
        fields = '__all__'

    def clean_products(self):
        products = self.cleaned_data.get('products')
        if products.count() > 4:
            raise forms.ValidationError("Faqatgina 4 ta top product tanlash mumkin!")
        return products
