
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin
from django.forms.fields import Field
GENDER_CHOICES=(
('male','MALE'),
('female','FEMALE'),
('other','OTHER')
)
RELATIONSHIP_CHOICES=(
    ("aunt","AUNT"),
    ("brother","BROTHER"),
    ("father","FATHER"),
    ("grandfather","GRANDFATHER"),
    ("grandmother","GRANDMOTHER"),
    ("guardian","GUARDIAN"),
    ("husband","HUSBAND"),
    ("mother","MOTHER"),
    ("other","OTHER"),
    ("sister","SISTER"),
    ("uncle","UNCLE"),
    ("wife","WIFE"),
)
BENIFICIARY_TYPE_CHOICES=(
    ("active", "ACTIVE"),
    ("inactive", "INACTIVE"),
    ("migrated", "MIGRATED"),
    ("deceased", "DECEASED"),
)
STATUS_OF_BENIFICIARY_CHOICES=(
    ("red", "RED"),
    ("yellow", "YELLOW"),
    ("green", "GREEN"),
)
ADDRESS_TYPE_CHOICES=(
    ('residence','RESIDENCE'),
    ('office','OFFICE'),
    ('permanent','PERMANENT'),
    ('present','PRESENT'),
    ('communication','COMMUNICATION'),
    ('native','NATIVE'),
    ('relative','RELATIVE'),
    ('temporary','TEMPORARY'),
)
DIAGONISIS_CHOICES=(
    ("bipolar","BIPOLAR"),
    ("schizophrenia","SCHIZOPHRENIA"),
    ("depression","DEPRESSION"),
    ("mania","MANIA"),
    ("anxiety disorders","ANXIETY DISORDERS"),
    ("panic disorder","PANIC DISORDER"),
    ("stress-related disorders","STRESS-RELATED DISORDERS"),
    ("dissociative disorders","DISSOCIATIVE DISORDERS"),
    ("dissociative amnesia","DISSOCIATIVE AMNESIA"),
    ("somatic symptom disorder","SOMATIC SYMPTOM DISORDER"),
    ("insomnia disorder","INSOMNIA DISORDER"),
    ("substance-related disorders","SUBSTANCE-RELATED DISORDERS"),
    ("obsessive-compulsive disorders (ocd)","OBSESSIVE-COMPULSIVE DISORDERS (OCD)"),
    ("personality disorders","PERSONALITY DISORDERS"),
    ("paranoid personality disorder","PARANOID PERSONALITY DISORDER"),
    ("other","OTHER"),
)
PURPOSE_OF_VISIT_CHOICES=(
    ("counselling","COUNSELLING"),
    ("mental health screening","MENTAL HEALTH SCREENING"),
    ("care giver training","CARE GIVER TRAINING"),
    ("livlihood training","LIVILIHOOD TRAINING"),
    ("other","OTHER"),
)
EDUCATION_HISTORY_CHOICES=(
    ("illiterate", "ILLITERATE"),
    ("upto class v", "UPTO CLASS V"),
    ("upto class viii", "UPTO CLASS VIII"),
    ("under matric", "UNDER MATRIC"),
    ("matriculation", "MATRICULATION"),
    ("degree", "DEGREE"),
    ("pg and above", "PG AND ABOVE"),
)
FAMILY_MONTHLY_INCOME_CHOICES=(
    ("less than rs.2500", "LESS THAN RS.2500"),
    ("rs.2500-rs.5000", "RS.2500-RS.5000"),
    ("rs.5000-rs.7000", "RS.5000-RS.7000"),
    ("rs.7000-rs.10000", "RS.7000-RS.10000"),
    ("rs.10000-rs.15000", "RS.10000-RS.15000"),
    ("rs.15000-rs.20000", "RS.15000-RS.20000"),
    ("more than rs.20000", "MORE THAN RS.20000"),
)
MARTIAL_STATUS_CHOICES=(
    ("unmarried","UNMARRIED"),
    ("married","MARRIED"),
    ("separated","SEPARATED"),
    ("widow","WIDOW"),
    ("remarried","REMARRIED"),
    )
DURATION_OF_ILLNESS_CHOICES=(
    ("sudden(few days or week)","SUDDEN(FEW DAYS OR WEEK)"),
    ("acute(few weeks to a month)","ACUTE(FEW WEEKS TO A MONTH)"),
    ("indidious(over many months)","INDIODIOUS(OVER MANY MONTHS)"),
    ("not applicable(eg epilepsy/mr)","NOT APPLICABLE(EG EPILEPSY/MR)"),
    ("unclear","UNCLEAR"),
)
PAST_PYSCHIATRIC_ILLNESS_CHOICES=(
    ("absent","ABSENT"),
    ("present","PRESENT"),
    ("unclear","UNCLEAR"),
)
PURPOSE_OF_VISIT_CHOICES=(
    ("","PATIENT FOLLOW UP"),
    ("","PATIENT COUNSELLING"),
    ("","CARE GIVER COUNSELLING"),
    ("","AWARENESS MEETING"),
    ("","LIVILIHOOD REHABILITATION"),
    ("","MONITORING"),
    ("","MEETING WITH VILLAGE LEVEL COMMITTEE"),
    ("","OTHER"),
)
DIAGNOSED_BY_CHOICES=(
    ("","Dr.J K Nath"),
    ("","Dr.P Kalita"),
    ("","Dr.Iftikar Hussain"),
    ("","Dr.Sujata Borkakoty"),
    ("","Others"),
)
DESIGNATION_CHOICES=(
    ("","Village committe member"),
    ("","ASHA"),
    ("","Anganwadi"),
    ("","ANM"),
    ("","Neighbours"),
    ("","Village shopkeeper"),
    ("","Other"),
)
BLOOD_GROUP_CHOICES=(
    ("","A+ve"),
    ("","B+ve"),
    ("","O+ve"),
    ("","AB+ve"),
    ("","A-ve"),
    ("","B-ve"),
    ("","O-ve"),
    ("","AB-ve"),
)
BIRTH_CHOICES=(
    ("","Normal"),
    ("","Abnormal"),
    ("","Other"),
)
DISABILITY_CHOICES=(
    ("","Locamator"),
    ("","Low vision"),
    ("","Blindness"),
    ("","Hearing impairment"),
    ("","Mental retardation"),
    ("","Mental illness"),
)
class Beneficiary(models.Model):
    image=models.ImageField(upload_to='home/images/',blank=True,null=True)
    name = models.CharField(max_length=200)
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,default='male')
    dob=models.DateField()
    registrationDate=models.DateField()
    uidOrAadhaar=models.CharField(blank=True,max_length=12,null=True)
    careGiversName=models.CharField(max_length=200,blank=True,null=True)
    reletionship=models.CharField(max_length=200,choices=RELATIONSHIP_CHOICES,default='other',blank=True,null=True)
    beneficiaryType=models.CharField(max_length=200,choices=BENIFICIARY_TYPE_CHOICES,default='active')
    statusOfBeneficiary=models.CharField(max_length=200,choices=STATUS_OF_BENIFICIARY_CHOICES,default='red')
    address=models.TextField(blank=True,null=True)
    district=models.CharField(max_length=200,blank=True,null=True)
    city=models.CharField(max_length=200)
    pinCode=models.CharField(max_length=200,blank=True,null=True)
    addressType=models.CharField(max_length=200,choices=ADDRESS_TYPE_CHOICES,blank=True,null=True)
    phone=models.CharField(max_length=13,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    diagonisis=models.CharField(max_length=200,choices=DIAGONISIS_CHOICES)
    diagnosedBy=models.CharField(max_length=200,choices=DIAGNOSED_BY_CHOICES,default="")
    informedBy=models.CharField(max_length=200,default='')
    designation=models.CharField(max_length=200,choices=DESIGNATION_CHOICES,default="")
    symptomsAsInformed=models.TextField(blank=True,null=True)
    educationHistory=models.CharField(max_length=200,choices=EDUCATION_HISTORY_CHOICES)

    maritialStatus=models.CharField(max_length=200,choices=MARTIAL_STATUS_CHOICES,blank=True,null=True)
    occupation=models.CharField(max_length=200,blank=True,null=True)
    skill=models.CharField(max_length=200,blank=True,null=True)
    birth=models.CharField(max_length=200,choices=BIRTH_CHOICES,blank=True,null=True)
    durationOfIllness=models.CharField(max_length=200,choices=DURATION_OF_ILLNESS_CHOICES,blank=True,null=True)
    pastPyschiatricIllness=models.CharField(max_length=200,choices=PAST_PYSCHIATRIC_ILLNESS_CHOICES,blank=True,null=True)
    gp=models.CharField(max_length=200)
    village=models.CharField(max_length=200)
    family_history_of_MI_present_or_absent=models.BooleanField(default=False)
    if_present_schizophrenia_or_mania_or_depression=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Beneficiaries"
class Patient(models.Model):
    name = models.CharField(max_length=200)
    purpose_of_visit_for_old_paitent=models.CharField(max_length=200,choices=PURPOSE_OF_VISIT_CHOICES,blank=True,null=True)
    is_new_patient=models.BooleanField(default=False)
    action_planned_for_new_patient=models.CharField(max_length=200,blank=True,null=True)
    symptoms_of_new_patient=models.TextField(blank=True,null=True)
    note_on_old_patient=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class Report(models.Model):
    name_of_new_patients=models.ManyToManyField(Patient,blank=True,null=True)
    name_of_old_patients=models.ManyToManyField(Patient,blank=True,null=True,related_name='old_patients')
    place_visited=models.CharField(max_length=200)
    no_of_family_members=models.IntegerField(default=0)
    no_of_siblings=models.IntegerField(default=0)
    familyMonthlyIncome=models.CharField(max_length=200,choices=FAMILY_MONTHLY_INCOME_CHOICES,blank=True,null=True)
    height=models.FloatField(default=0)
    weight=models.FloatField(default=0)
    # @property
    # def BMI(self):
    #     return self.weight/(self.height*self.height)
    blood_group=models.CharField(max_length=200,choices=BLOOD_GROUP_CHOICES,blank=True,null=True)
    identification_mark=models.CharField(max_length=200,blank=True,null=True)
    notes=models.TextField(blank=True,null=True)
    date_of_visit=models.DateField()
    date=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.date)

class Camp(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField(validators=[MaxValueValidator(150),MinValueValidator(1)])
    sex=models.CharField(max_length=200,choices=GENDER_CHOICES)
    village=models.CharField(max_length=200)
    diagonisis=models.CharField(max_length=200,choices=DIAGONISIS_CHOICES)
    identification_date=models.DateField()
    name_of_medicine_taking=models.CharField(max_length=200)
    screening_camp_date=models.DateField()
    name_of_psychiatrist=models.CharField(max_length=200)
    advice_by_psychiatrist=models.TextField()
    counselling_by=models.CharField(max_length=200)
    color_suggested_by_psychiatrist=models.CharField(max_length=200,choices=STATUS_OF_BENIFICIARY_CHOICES)
    next_review_date=models.DateField()
    idendified=models.BooleanField(default=False)
    submitted_by=models.CharField(max_length=200)
    upload_prescription=models.FileField(upload_to='home/files/',blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Patient Camp'

class ScreeningCamp(models.Model):
    beneficiary=models.ForeignKey(Beneficiary,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    dob=models.DateField()
    gender=models.CharField(max_length=200,choices=GENDER_CHOICES)
    fatherName=models.CharField(max_length=200)
    motherName=models.CharField(max_length=200)
    careGiver=models.CharField(max_length=200)
    relationship=models.CharField(max_length=200,choices=RELATIONSHIP_CHOICES)
    address=models.TextField()
    village=models.CharField(max_length=200)
    phone=models.CharField(max_length=13,blank=True,null=True)
    designation=models.CharField(max_length=200,choices=DESIGNATION_CHOICES)
    disability=models.CharField(max_length=200,choices=DISABILITY_CHOICES)
    visitedBy=models.CharField(max_length=200)
