from tabnanny import check
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from myapp.models import *

# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def RegisterPage(request):
    return render(request, "app/register.html")

def RegisterUser(request):
    if request.method == "POST":
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = make_password(request.POST['password'])
        cpwd = (request.POST['cpassword'])
        
        user = User.objects.filter(email = email).first()
        
        if(not user):
            if check_password(cpwd,pwd):
                User.objects.create(email =email,firstname = fname, lastname = lname, password = pwd);
                return redirect(IndexPage)
            else:
                msg ="*password doesn't match*"
        else:
            msg ="*user already exists*"
        
    return render(request, "app/register.html",{'msg':msg})

def LoginPage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    
    email = request.POST['email']
    pwd = request.POST['password']
    user = User.objects.filter(email = email).first()
    if(user):
        if(check_password(pwd,user.password)):
            request.session['id'] = user.id
            request.session['firstname'] = user.firstname
            request.session['lastname'] = user.lastname
            request.session['email'] = email
            
            return redirect(IndexPage)
        else:
            msg = "*Incorrect password*"
    else:
        msg = "*User does not exist*"
    
    return render(request, "app/login.html",{'msg':msg})

def LogoutUser(request):
    request.session.flush()
    return  redirect(LoginPage)

def ContactPage(request):
           
    return render(request,"app/contact.html")

def SubmitQuery(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        query = request.POST['message']
        user = User.objects.filter(email=email).first()
        if(user):
            q = Query.objects.create(userid = user, Contact = contact, Message = query)
            return render(request,"app/thankyou.html")
        else:
            msg = "*Enter valid email address*"
        return render(request,"app/contact.html",{'msg':msg})
        

def AboutUsPage(request):
    return render(request,"app/aboutus.html")