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
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import os
from django.conf import settings

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL     # Typically /static/
    #static Root
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path
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
    '',
    'Name',
    'Gender',
    'DOB',
    'Registration date',
    'Id type',
    'Id Number',
    'Care Givers Name',
    'Relationship',
    'Beneficiary type',
    'Status Of Beneficiary',
    'District',
    'Village',
    'Pin Code',
    'Address Type',
    'Phone Number',
    'Email',
    'Diagnosis',
    'Diagnosed By',
    'Informed By',
    'Designation',
    'Symptoms',
    'Education History',
    'Maritial Status',
    'Occupation',
    'Skill',
    'Birth Type',
    'Duration of illness',
    'Past Pyschiatric Illness',
    'If Family History Of MI present'
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
                form.cleaned_data["care_giver"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).care_givers_name
                form.cleaned_data["relationship"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).relationship
                # form.cleaned_data["address"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).address
                form.cleaned_data["village"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).village
                form.cleaned_data["phone"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).phone
                form.cleaned_data["designation"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).designation
                form.cleaned_data["diagonisis"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).diagonisis
                form.cleaned_data["diagnosed_by"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).diagnosed_by
                form.cleaned_data["education_history"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).education_history
                form.cleaned_data["maritial_status"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).maritial_status
                form.cleaned_data["occupation"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).occupation
                form.cleaned_data["skill"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).skill
                form.cleaned_data["birth"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).birth
                form.cleaned_data["duration_of_illness"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).duration_of_illness
                form.cleaned_data["past_psychiatric_illness"]=Beneficiary.objects.get(id=request.POST.get('beneficiary')).past_pyschiatric_illness
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
 
    columns =[
    'db_id',
    'beneficiary',
    'name',
    'dob',
    'gender',
    'father_name',
    'mother_name',
    'care_giver',
    'relationship',
    'symptoms',
    'diagnosis',
    'diagnosed_by',
    'education_history',
    'maritial_status',
    'occupation',
    'skill',
    'birth',
    'duration_of_illness',
    'past_pyschiatric_illness',
    'village',
    'phone',
    'designation',
    'disability',
    'visited_by',
    'blood_pressure',
    'height',
    'weight',
    'name_of_psychiatrist',
    'name_of_medicine_taking',
    'color_suggested_by_psychiatrist',
    'next_review_date',
    'identified',
    'prescription html(please ignore)',
    'date_of_camp']
 
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

def export_prescription(request):
    content={
        "patients":ScreeningCamp.objects.all()
    }
    if request.method=="POST":

        patient_id=request.POST.get('patient')
        patient=ScreeningCamp.objects.get(id=patient_id)
        template_path = 'home/prescription.html'
        context = {'patient':patient}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="prescription.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response,encoding='utf-8' , link_callback=link_callback)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    return render(request,"home/export_prescription.html",content)

# def render_pdf_view(request):
#     template_path = 'home/prescription.html'
#     context = {'myvar': 'Hello World'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response