from django.shortcuts import render
from blog.models import AboutMe,Education,Experience,Achivement,Title,Skill,Projects,Hobby
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from blog.forms import Subscribe
from django.core.mail import send_mail
# Create your views here.
def index(request):
    ls=Title.objects.all()
    lst=AboutMe.objects.all()
    lst1=Education.objects.all()
    lst2=Experience.objects.all()
    lst3=Achivement.objects.all()
    return render(request,'index.html',{'ls':ls,'lst':lst,'lst1':lst1,'lst2':lst2,'lst3':lst3})

def home(request):
    lst=AboutMe.objects.all()
    lst1=Education.objects.all()
    lst2=Experience.objects.all()
    lst3=Achivement.objects.all()
    return render(request,'index.html',{'lst':lst,'lst1':lst1,'lst2':lst2,'lst3':lst3})
    
def about(request):
    lst=AboutMe.objects.all()
    lst1=Education.objects.all()
    lst2=Experience.objects.all()
    lst3=Achivement.objects.all()
    return render(request,'about.html',{'lst':lst,'lst1':lst1,'lst2':lst2,'lst3':lst3})

def project(request):
    return render(request,'project.html')

def education(request):
    lst1=Education.objects.all()
    return render(request,'education.html',{'lst1':lst1})

def service(request):
    return render(request,'service.html')

def subscribe(request):
    form=Subscribe(request.POST or None)
    if form.is_valid():
        name=request.POST.get("contact_name")
        email=request.POST.get("contact_email")
        content=request.POST.get("content")

        subject="Hello from Krunal."
        from_email=settings.EMAIL_HOST_USER
        user_email=email
        to_list=[user_email,from_email]
        send_mail(subject,content,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    
    return render(request,'subscribe.html',{'form':form})

def thankyou(request):
    return render(request,'thankyou.html')
def blog(request):
    return render(request,'blog.html')

def resume(request):
    ls=Title.objects.all()
    lst=AboutMe.objects.all()
    lst1=Education.objects.all()
    lst2=Experience.objects.all()
    lst3=Achivement.objects.all()
    lst4=Skill.objects.all()
    lst5=Projects.objects.all()
    lst6=Hobby.objects.all()
    return render(request,'resume.html',{'ls':ls,'lst':lst,'lst1':lst1,'lst2':lst2,'lst3':lst3,'lst4':lst4,'lst5':lst5,'lst6':lst6})
