from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_beneficiary/',views.add_beneficiary,name='add_beneficiary'),
    path('export_beneficiary_xls/',views.export_beneficiary_xls,name='export_beneficiary_xls'),
    path('export_scamp_xls/',views.export_scamp_xls,name='export_scamp_xls'),
    path('export_beneficiary_temp/',views.export_beneficiary_temp,name='export_beneficiary_temp'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('add_report',views.add_report,name='add_report'),
    path('add_patient_camp',views.add_patient_camp,name='add_patient_camp'),
    path('add_screening_camp',views.add_screening_camp,name='add_screening_camp'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]