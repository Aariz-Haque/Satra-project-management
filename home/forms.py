from attr import field
from django.forms import ModelForm
from django.forms.fields import *
from django.contrib.admin.widgets import AdminDateWidget
from .models import Beneficiary, Patient, Report

class BeneficiaryForm(ModelForm):
    class Meta:
        model=Beneficiary
        dob=DateField(widget=AdminDateWidget)
        registrationDate=DateField(widget=AdminDateWidget)
        fields='__all__'

class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class ReportForm(ModelForm):
    class Meta:
        model=Report
        fields='__all__'

