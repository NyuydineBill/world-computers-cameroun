from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields= '__all__'
class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields= '__all__'
class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields= '__all__'
class SmartTVForm(forms.ModelForm):
    class Meta:
        model = SmartTV
        fields= '__all__'
class OthersForm(forms.ModelForm):
    class Meta:
        model = Others
        fields= '__all__'
class AllInOneForm(forms.ModelForm):
    class Meta:
        model = AllInOne
        fields= '__all__'

class TestimoniesForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = "__all__"
