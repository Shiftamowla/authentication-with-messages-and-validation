from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse,Http404
from myapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError


def base(req):
    return render(req,'base.html')

def home(req):
    return render(req,'home.html')

@login_required
def listresume(req):
    user=req.user
    if user.user_type == "admin":
        data=ResumeModel.objects.all()
        return render(req,'listresume.html',{'data': data})
    else:
        return render(req,'error.html')
    
def skill_list(req):
    current_user=req.user
    myskill=Skills_Model.objects.filter(user=current_user)
    myedu=Education_Model.objects.filter(user=current_user)
    myexp=Experience_Model.objects.filter(user=current_user)
    myint=Interest_Model.objects.filter(user=current_user)
    mylang=Language_Model.objects.filter(user=current_user)

    return render(req, 'skill_list.html',{'myskill':myskill,'myedu':myedu,'myexp':myexp,'myint':myint,'mylang':mylang})
def Education_list(req):
    current_user=req.user
    myedu=Education_Model.objects.filter(user=current_user)
    return render(req, 'skill_list.html',{'myedu':myedu})
def Experience_list(req):
    current_user=req.user
    myexp=Experience_Model.objects.filter(user=current_user)
    return render(req, 'skill_list.html',{'myexp':myexp})
def Interest_list(req):
    current_user=req.user
    myint=Interest_Model.objects.filter(user=current_user)
    return render(req, 'skill_list.html',{'myint':myint})
def Language_list(req):
    current_user=req.user
    mylang=Language_Model.objects.filter(user=current_user)
    return render(req, 'skill_list.html',{'mylang':mylang})
     
@login_required
def addresume(req):
    all_user=Custom_user.objects.all()

    if req.method=='POST':
        id=req.POST.get('user_id')
        user_object=Custom_user.objects.get(id=id)

        add=ResumeModel(
            user=user_object,
            Gender=req.POST.get('Gender'),
            linkdin=req.POST.get('linkdin'),
            designation=req.POST.get('designation'),
            contact=req.POST.get('contact'),
            img=req.FILES.get('img'),

        )
        add.save()
        return redirect ('listresume')
    return render(req,'addresume.html',{'data':all_user})
def profilepage(req):
    current_user=req.user


    resume=ResumeModel.objects.filter(user=current_user)
    Education=Education_Model.objects.filter(user=current_user)
    Experience=Experience_Model.objects.filter(user=current_user)
    Interest=Interest_Model.objects.filter(user=current_user)
    Skills=Skills_Model.objects.filter(user=current_user)
    Language=Language_Model.objects.filter(user=current_user)
    text={
        'resume':resume,
        'Education':Education,
        'Experience':Experience,
        'Interest':Interest,
        'Skills':Skills,
        'Language':Language,
    }
    return render(req,'resume.html',text)

def currentresume(req):
    if req.user.user_type == 'viewer':
     current_user=req.user

    if req.method=='POST':

        add=ResumeModel(
            user=current_user,
            Gender=req.POST.get('Gender'),
            linkdin=req.POST.get('linkdin'),
            designation=req.POST.get('designation'),
            contact=req.POST.get('contact'),
            img=req.FILES.get('img'),

        )
        add.save()
        current_user.first_name=req.POST.get('first_name')
        current_user.last_name=req.POST.get('last_name')

        current_user.save()


    return render(req,'currentresume.html')

def addSkill(req):
    current_user=req.user

    skill=intermediate_skillmodel.objects.all()


    if req.method=='POST':
        skill_id=req.POST.get('skill_id')

        skill_object=get_object_or_404(intermediate_skillmodel,id=skill_id)
        if Skills_Model.objects.filter(user=current_user,skill_name=skill_object.skill_name).exists():
            return HttpResponse('skill already exist')
        else:
                    add=Skills_Model(
            user=current_user,
            skill_name=skill_object,
            proficiency_level=req.POST.get('proficiency_level'),

        )
        add.save()
        return redirect ('skill_list')


    return render(req,'addSkill.html',{'skill':skill})


# Edit Skill Function

def editSkill(req,id):
    allskill=Skills_Model.objects.get(id=id)
    skill=intermediate_skillmodel.objects.all()
    
    current_user = req.user
    
    if req.method=='POST':
            Skill_Id = req.POST.get("Skill_Id")
            Skill_Level = req.POST.get("Skill_Level")
            
            MyObj = get_object_or_404(intermediate_skillmodel, id=Skill_Id)
            
            skill = Skills_Model(
                id=id,
                user=current_user,
                skill_name=MyObj.My_Skill_Name,  
                Skill_Level=Skill_Level,
            )
            skill.save()
            return redirect("skill_list")
    
    context={
        "allskill":allskill,
        "skill":skill,
        "proficiency_level":Skills_Model.proficiency_level
    }

    return render(req,'editSkill.html',context)


#Add Eduction Function

def addEducation(req):
    current_user=req.user

    edu=intermediate_Educationmodel.objects.all()


    if req.method=='POST':
        edu_id=req.POST.get('edu_id')

        eduobj=get_object_or_404(intermediate_Educationmodel,id=edu_id)
        if Education_Model.objects.filter(user=current_user,type=eduobj.type).exists():
            return HttpResponse('Education already exist')
        else:
            add=Education_Model(
            user=current_user,
            type=eduobj,
            start_date=req.POST.get('start_date'),
            end_date=req.POST.get('end_date'),

        )
        add.save()
        return redirect ('skill_list')
    return render(req,'addEducation.html',{'edu':edu})



# Add Experience Function

def addExperience(req):
    current_user=req.user

    exp=intermediate_Experiencemodel.objects.all()


    if req.method=='POST':
        exp_id=req.POST.get('exp_id')

        exp_object=get_object_or_404(intermediate_Experiencemodel,id=exp_id)
        if Experience_Model.objects.filter(user=current_user,title=exp_object.title).exists():
            return HttpResponse('Experience already exist')
        else:
            add=Experience_Model(
            user=current_user,
            title=exp_object,
            start_date=req.POST.get('start_date'),
            end_date=req.POST.get('end_date'),

        )
        add.save()
        return redirect ('skill_list')
    return render(req,'addExperience.html',{'exp':exp})

def addsInterest(req):
    current_user=req.user

    inte=intermediate_Interestmodel.objects.all()


    if req.method=='POST':
        inte_id=req.POST.get('inte_id')

        int_object=get_object_or_404(intermediate_Interestmodel,id=inte_id)
        if Interest_Model.objects.filter(user=current_user,title=int_object.title).exists():
            return HttpResponse('Interest already exist')
        else:
            add=Interest_Model(
            user=current_user,
            title=int_object,

        )
        add.save()
        return redirect ('skill_list')
    return render(req,'addsInterest.html',{'inte':inte})



def addsLanguage(req):
    current_user=req.user

    lan=intermediate_Languagemodel.objects.all()


    if req.method=='POST':
        la_id=req.POST.get('la_id')

        la_object=get_object_or_404(intermediate_Languagemodel,id=la_id)
        if Language_Model.objects.filter(user=current_user,language_name=la_object.language_name).exists():
            return HttpResponse('Language already exist')
        else:
            add=Language_Model(
            user=current_user,
            language_name=la_object,
            proficiency_level=req.POST.get('proficiency_level'),

        )
        add.save()
        return redirect ('skill_list')
    return render(req,'addsLanguage.html',{'lan':lan})



def resume(req,id):
    data=get_object_or_404(Custom_user,id=id)

    resume=ResumeModel.objects.filter(user=data)
    Education=Education_Model.objects.filter(user=data)
    Experience=Experience_Model.objects.filter(user=data)
    Interest=Interest_Model.objects.filter(user=data)
    Skills=Skills_Model.objects.filter(user=data)
    Language=Language_Model.objects.filter(user=data)

    text={
        'resume':resume,
        'Education':Education,
        'Experience':Experience,
        'Interest':Interest,
        'Skills':Skills,
        'Language':Language,
    }
    return render(req,'resume.html',text)

def edit(req,id):
    alluser=Custom_user.objects.all()
    data=ResumeModel.objects.filter(id=id)
    if req.method=='POST':
        id=req.POST.get('id')
        id=req.POST.get('user_id')
        designation=req.POST.get('designation')
        Gender=req.POST.get('Gender')
        contact=req.POST.get('contact')
        linkdin=req.POST.get('linkdin')
        img=req.FILES.get('img')
        oldimg=req.POST.get('oldimg')

        user_object=Custom_user.objects.get(id=id)

        add=ResumeModel(
            id=id,
            user=user_object,
            designation=designation,
            Gender=Gender,
            contact=contact,
            linkdin=linkdin,

        )
        if img:
          add.img=img
          add.save()
        else:
         add.img=oldimg
         add.save()
        return redirect ('listresume')
    context={
        'alluser':alluser,
        'data':data
    }
    return render (req,'edit.html',context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.warning(request, "Both username and password are required")
            return render(request, "loginPage.html")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect("home")
        else:
            messages.warning(request, "Invalid username or password")

    return render(request, "loginPage.html")

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_type = request.POST.get("usertype")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not all([username, email, user_type, password, confirm_password]):
            messages.warning(request, "All fields are required")
            return render(request, "signupPage.html")

        try:
            validate_email(email)
        except ValidationError:
            messages.warning(request, "Invalid email format")
            return render(request, "signupPage.html")

        if password != confirm_password:
            messages.warning(request, "Passwords do not match")
            return render(request, "signupPage.html")

        if len(password) < 4:
            messages.warning(request, "Password must be at least 8 characters long")
            return render(request, "signupPage.html")

        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            messages.warning(request, "Password must contain both letters and numbers")
            return render(request, "signupPage.html")

        try:
            user = Custom_user.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=password
            )
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("loginpage")
        except IntegrityError:
            messages.warning(request, "Username or email already exists")
            return render(request, "signupPage.html")

    return render(request, "signupPage.html")

def logoutpage(req):
    logout(req)
    messages.success(req, "Logged out successfully.")

    return redirect('loginpage')


def sdeletepage(req,id):
    data=Skills_Model.objects.filter(id=id)
    data.delete()
    return redirect('skill_list')
def edeletepage(req,id):
    data=Education_Model.objects.filter(id=id)
    data.delete()
    return redirect('skill_list')
def ldeletepage(req,id):
    data=Language_Model.objects.filter(id=id)
    data.delete()
    return redirect('skill_list')
def exdeletepage(req,id):
    data=Experience_Model.objects.filter(id=id)
    data.delete()
    return redirect('skill_list')
def ideletepage(req,id):
    data=Interest_Model.objects.filter(id=id)
    data.delete()
    return redirect('skill_list')