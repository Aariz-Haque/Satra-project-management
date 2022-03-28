from django.forms import ModelForm
from django.forms.fields import *
from django.contrib.admin import widgets
from .models import Beneficiary, Patient, Report, Camp,ScreeningCamp
from .minimaldate import MinimalSplitDateTimeMultiWidget

class BeneficiaryForm(ModelForm):
    class Meta:
        model=Beneficiary
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(BeneficiaryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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
    def __init__(self, *args, **kwargs):
        super(CampForm, self).__init__(*args, **kwargs)
        self.fields['screening_camp_date'].widget=widgets.AdminDateWidget()
        self.fields['next_review_date'].widget=widgets.AdminDateWidget()
        

class ScreeningCampForm(ModelForm):
    class Meta:
        model=ScreeningCamp
        fields=['beneficiary','name','dob','gender','father_name','mother_name','care_giver','relationship','symptoms','diagnosis','diagnosed_by','education_history','maritial_status','occupation','skill','birth','duration_of_illness','past_pyschiatric_illness','village','phone','designation','disability','visited_by','blood_pressure','height','weight','name_of_psychiatrist','name_of_medicine_taking','color_suggested_by_psychiatrist','next_review_date','identified','date_of_camp']
        widgets={
            'screening_camp_date':widgets.AdminDateWidget(),
            'next_review_date':widgets.AdminDateWidget(),

        }
        # fields['date_of_camp'].widget=widgets.AdminDateWidget()
        # fields['beneficiary'].label='Beneficiary(for old patient)'
    def __init__(self, *args, **kwargs):
        super(ScreeningCampForm, self).__init__(*args, **kwargs)
        self.fields['beneficiary'].label='Beneficiary(for old patient)'