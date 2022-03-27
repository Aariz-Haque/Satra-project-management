from datetime import datetime
from django.db import IntegrityError
from django.shortcuts import render,redirect,HttpResponse
from .models import Beneficiary,Camp,ScreeningCamp
from .forms import BeneficiaryForm,PatientForm,ReportForm,CampForm,ScreeningCampForm
import xlwt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
def login_user(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exit')
    return render(request,"home/login.html")
def logout_user(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/login/')
def home(request):
        return render(request,"home/home.html")

@login_required(login_url='/login/')
def add_beneficiary(request):
    form=BeneficiaryForm()
    if request.method=="POST":
        form=BeneficiaryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid beneficiary details')
    context={'form':form}
    return render(request,"home/add_beneficiary.html",context)

@login_required(login_url='/login/')
def export_beneficiary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="beneficiaries.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Beneficiaries')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = [
    'db_id',
    'Name',
    'Gender',
    'DOB',
    'Registration Date',
    'UID or Aadhaar',
    "Care Giver's Name",
    'Reletionship',
    'Beneficiary Type',
    'Status of Beneficiary',
    'Address',
    'District',
    'City',
    'Pin Code',
    'Address Type',
    'Phone',
    'Email',
    'Diagonisis',
    'Purpose of Visit',
    'Education History',
    'Family Monthly Income',
    'Maritial Status',
    'Duration of Illness',
    'Past Pyschiatric Illness',
    'G.P',
    'Village',
    'Family history of MI present or absent',
    'If Present Schizophrenia Or Mania Or Depression'
    ]
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = Beneficiary.objects.all().values_list()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if row[col_num].__class__.__name__ == 'date':
                obj=row[col_num].strftime('%d-%m-%Y')
            else:
                 obj=row[col_num]
            ws.write(row_num, col_num, obj, font_style) 
    wb.save(response)
    return response


@login_required(login_url='/login/')
def export_beneficiary_temp(request):
    return render (request,"home/export_beneficiary_temp.html")

@login_required(login_url='/login/')
def add_patient(request):
    form=PatientForm()
    if request.method=="POST":
        form=PatientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_report')
        else:
            messages.error(request, 'Invalid patient details')
    context={'form':form}

    return render(request,"home/add_patient.html",context)
@login_required(login_url='/login/')
def add_report(request):
    form=ReportForm()
    if request.method=="POST":
        form=ReportForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid report details')
    context={'form':form}
    return render(request,"home/add_report.html",context)
@login_required(login_url='/login/')
def add_patient_camp(request):
    form=CampForm()
    if request.method=="POST":
        form=CampForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid camp details')
    context={'form':form}
    return render(request,"home/add_patient_camp.html",context)
@login_required(login_url='/login/')
def add_screening_camp(request):
    form=ScreeningCampForm()
    if request.method=="POST":
        form=ScreeningCampForm(request.POST,request.FILES)
        if form.is_valid():
            if request.POST.get('beneficiary')!='':
                form.cleaned_data["name"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).name
                form.cleaned_data["dob"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).dob
                form.cleaned_data["gender"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).gender
                form.cleaned_data["careGiver"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).careGiversName
                form.cleaned_data["relationship"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).reletionship
                form.cleaned_data["address"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).address
                form.cleaned_data["village"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).village
                form.cleaned_data["phone"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).phone
                form.cleaned_data["designation"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).designation
            form2=ScreeningCampForm(form.cleaned_data)
            print(form.cleaned_data)
            form2.save()
            
            return redirect('home')
        else:
            messages.error(request, 'Invalid screening camp details')
    context={'form':form}
    return render(request,"home/add_screening_camp.html",context)

def export_scamp_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="camps.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Camps')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = [
    'db_id',
    'beneficiary_code',
    'Name',
    'DOB',
    'Gender',
    'Father name',
    'Mother name',
    'Care Giver',
    'Relationship',
    'Address',
    'Village',
    'Phone',
    'Designation',
    'Disability',
    'Visited By',
    ]
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = ScreeningCamp.objects.all().values_list()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if row[col_num].__class__.__name__ == 'date':
                obj=row[col_num].strftime('%d-%m-%Y')
            else:
                 obj=row[col_num]
            ws.write(row_num, col_num, obj, font_style) 
    wb.save(response)
    return response
