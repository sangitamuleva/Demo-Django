from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Category
        fields = '__all__'

class SubCategoryForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = SubCategory
        fields = '__all__'
