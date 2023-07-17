from django.forms import ModelForm
from .models import Addservice

class Service(ModelForm):
    class meta:
        model = Addservice
        fields = '__all__'