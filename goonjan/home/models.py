from mmap import mmap
from re import M
from django.db import models

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
    ("","PAITENT FOLLOW UP"),
    ("","PAITENT COUNSELLING"),
    ("","CARE GIVER COUNSELLING"),
    ("","AWARENESS MEETING"),
    ("","LIVILIHOOD REHABILITATION"),
    ("","MONITORING"),
    ("","MEETING WITH VILLAGE LEVEL COMMITTEE"),
    ("","OTHER"),
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
    purposeOfVisit=models.CharField(max_length=200,choices=PURPOSE_OF_VISIT_CHOICES,blank=True,null=True)
    educationHistory=models.CharField(max_length=200,choices=EDUCATION_HISTORY_CHOICES)
    familyMonthlyIncome=models.CharField(max_length=200,choices=FAMILY_MONTHLY_INCOME_CHOICES,blank=True,null=True)
    maritialStatus=models.CharField(max_length=200,choices=MARTIAL_STATUS_CHOICES,blank=True,null=True)
    durationOfIllness=models.CharField(max_length=200,choices=DURATION_OF_ILLNESS_CHOICES,blank=True,null=True)
    pastPyschiatricIllness=models.CharField(max_length=200,choices=PAST_PYSCHIATRIC_ILLNESS_CHOICES,blank=True,null=True)
    gp=models.CharField(max_length=200)
    village=models.CharField(max_length=200)
    family_history_of_MI_present_or_absent=models.BooleanField(default=False)
    if_present_schizophrenia_or_mania_or_depression=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    purpose_of_visit_for_old_paitent=models.CharField(max_length=200,choices=PURPOSE_OF_VISIT_CHOICES,blank=True,null=True)
    is_new_patient=models.BooleanField(default=False)
    action_planned_for_new_patient=models.CharField(max_length=200,blank=True,null=True)
    symptoms_of_new_patient=models.TextField(blank=True,null=True)
    note_on_new_patient=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class Report(models.Model):
    name_of_new_patients=models.ManyToManyField(Patient,blank=True,null=True)
    name_of_old_patients=models.ManyToManyField(Patient,blank=True,null=True,related_name='old_patients')
    place_visited=models.CharField(max_length=200)
    notes=models.TextField(blank=True,null=True)
    date_of_visit=models.DateField()
    date=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.date)
