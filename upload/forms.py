import csv
from django import forms
from upload.models import Clients

class Clients(forms.ModelForm):
   class Meta:
       model =  Clients
       fields = "__all__"
