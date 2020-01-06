from django.db import models
from datetime import date
# Create your models here.
class Title(models.Model):
    name=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    mail=models.EmailField(max_length=300,null=True,blank=True,unique=True)
    f_url=models.URLField(blank=True)
    phone=models.PositiveIntegerField(null=True)
    def __str__(self):
        return '%s'% (self.name)
    
class AboutMe(models.Model):
    about_me=models.TextField(max_length=500)
    intro=models.TextField(max_length=500)
    photo=models.FileField(blank=True)

    def __str__(self):
        return '%s'% (self.about_me)


class Education(models.Model):
    name=models.CharField(max_length=30)
    speci=models.CharField(max_length=30)
    colleg=models.CharField(max_length=30)
    s_date=models.DateField(default=date.today)
    e_date=models.DateField(default=date.today)
    marks=models.FloatField()

    def __str__(self):
        return '%s'% (self.name)
j_list=(('I','Internship'),('F','Full Time'),('P','Part Time'))
class Experience(models.Model):
    name_o=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    type_j=models.CharField(max_length=1,null=True,blank=True,choices=j_list)
    s_date=models.DateField(default=date.today)
    e_date=models.DateField(default=date.today)

    def __str__(self):
        return '%s'% (self.name_o)


class Achivement(models.Model):
    name_a=models.CharField(max_length=30)
    a_date=models.DateField(default=date.today)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return '%s'% (self.name_a)
    
class Skill(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return '%s'% (self.name)

class Projects(models.Model):
    title=models.CharField(max_length=30)
    s_date=models.DateField(default=date.today)
    e_date=models.DateField(default=date.today)
    intro=models.TextField(max_length=500)
    role=models.CharField(max_length=30)
    skills=models.CharField(max_length=300)
    d_b=models.CharField(max_length=30)
    ides=models.CharField(max_length=30)

    def __str__(self):
        return '%s'% (self.title)


class Hobby(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return '%s'% (self.name)
    
    
    
