from django.db import models
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('others', 'others')
)
DICT_CHOICES = (
    ('Alappuzha', 'Alappuzha'),
    ('Ernakulam', 'Ernakulam'),
    ('Idukki', 'Idukki'),
    ('Kannur', 'Kannur'),
    ('Malappuram', 'Malappuram'),
    ('Kozhikode', 'Kozhikode')
)
ACCOUNT_CHOICES = (
    ('savaing account', 'savaing account'),
    ('current account', 'current account'),
    ('checking account', 'checking account')
)

MODEL_CATEGORIES = (
        ('debit card', 'debit card'),
        ('credit card', 'credit card'),
        ('cheque', 'cheque'),
    )
class delts(models.Model):      
    name=models.CharField(max_length=500, blank=True, null=True)
    dob=models.DateField(null=True, blank=True)
    gender= models.CharField(choices=GENDER_CHOICES, max_length=100)
    age=models.CharField(max_length=200, null=True, blank=True)
    p_number= models.CharField(max_length=100, null=True, blank=True)
    mail= models.EmailField(null=True, blank=True)
    addrss= models.CharField(max_length=300, null=True, blank=True)
    dist= models.CharField(choices=DICT_CHOICES,max_length=100, )
    accounts= models.CharField(choices=ACCOUNT_CHOICES,max_length=100)
    materials= models.CharField(choices=MODEL_CATEGORIES,max_length=200, null=True, blank=True)
