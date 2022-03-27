from django.forms import ModelForm
from django.forms.fields import *
from django.contrib.admin import widgets
from .models import Beneficiary, Patient, Report, Camp,ScreeningCamp
from .minimaldate import MinimalSplitDateTimeMultiWidget

class BeneficiaryForm(ModelForm):
    class Meta:
        model=Beneficiary
        fields='__all__'

class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class ReportForm(ModelForm):

    class Meta:
        model=Report
        fields='__all__'
        widgets = {
            'date_of_visit': widgets.AdminDateWidget(),
        }
        date_of_visit = DateTimeField(widget=MinimalSplitDateTimeMultiWidget())
    # def __init__(self, *args, **kwargs):
    #     super(ReportForm, self).__init__(*args, **kwargs)
    #     self.fields['name_of_new_patients'].queryset = Patient.objects.filter(is_new_patient=True)
    #     self.fields['name_of_old_patients'].queryset = Patient.objects.filter(is_new_patient=False)
    #     self.fields['date_of_visit'].widget=widgets.AdminDateWidget()

class CampForm(ModelForm):
    class Meta:
        model=Camp
        fields='__all__'
        widgets={
            'screening_camp_date':widgets.AdminDateWidget(),
            'next_review_date':widgets.AdminDateWidget(),

        }
    # def __init__(self, *args, **kwargs):
    #     super(CampForm, self).__init__(*args, **kwargs)
    #     self.fields['screening_camp_date'].widget=widgets.AdminDateWidget()
    #     self.fields['next_review_date'].widget=widgets.AdminDateWidget()

class ScreeningCampForm(ModelForm):
    class Meta:
        model=ScreeningCamp
        fields=['name','dob','gender','fatherName','motherName','careGiver','relationship','address','village','phone','designation','disability','visitedBy','blood_pressure','height','weight','date_of_camp']
        widgets={
            'screening_camp_date':widgets.AdminDateWidget(),
            'next_review_date':widgets.AdminDateWidget(),

        }
    # def __init__(self, *args, **kwargs):
    #     super(ScreeningCampForm, self).__init__(*args, **kwargs)
    #     self.fields['screening_camp_date'].widget=widgets.AdminDateWidget()
    #     self.fields['next_review_date'].widget=widgets.AdminDateWidget()
