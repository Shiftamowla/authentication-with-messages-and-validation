from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
    
class ResumeModel(models.Model):
    gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    user=models.OneToOneField(Custom_user,null=True,on_delete=models.CASCADE)


    linkdin=models.URLField(max_length=100, null=True)
    Gender=models.CharField(choices=gender,max_length=100, null=True)
    contact=models.CharField(max_length=100, null=True)
    designation=models.CharField(max_length=100, null=True)
    summary=models.CharField(max_length=100, null=True)
    img=models.ImageField(upload_to='Media/img',null=True)

    def  __str__(self):
        return f"{self.user}-{self.designation}"
    

class Education_Model(models.Model):
    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    type=models.CharField(max_length=100, null=True)
    start_date=models.DateField(max_length=100, null=True)
    end_date=models.DateField(max_length=100, null=True)
    def  __str__(self):
        return f"{self.user.first_name}-{self.type}"

class Experience_Model(models.Model):
    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100, null=True)
    start_date=models.DateField(max_length=100, null=True)
    end_date=models.DateField(max_length=100, null=True)

    def  __str__(self):
        return f"{self.user.first_name}-{self.title}"

class Interest_Model(models.Model):
    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100, null=True)

    def  __str__(self):
        return f"{self.user.first_name}-{self.title}"

class Skills_Model(models.Model):
    proficiency=[
        ('high','High'),
        ('mideum','mideum'),
        ('low','Low')
    ]

    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=100, null=True)
    proficiency_level=models.CharField(choices=proficiency,max_length=100, null=True)

    class Meta:
        unique_together=['user','skill_name']

    def  __str__(self):
        return f"{self.user.first_name}-{self.skill_name}"

class Language_Model(models.Model):
    proficiency=[
        ('high','High'),
        ('mideum','mideum'),
        ('low','Low')
    ]

    user=models.ForeignKey(Custom_user,null=True,on_delete=models.CASCADE)
    language_name=models.CharField(max_length=100, null=True)
    proficiency_level=models.CharField(choices=proficiency,max_length=100, null=True)

    def  __str__(self):
        return f"{self.user.first_name}-{self.language_name}"
    
class intermediate_skillmodel(models.Model):
    skill_name=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.skill_name}"
    
class intermediate_Educationmodel(models.Model):
    type=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.type}"
    
class intermediate_Experiencemodel(models.Model):
    title=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.title}"
    
class intermediate_Interestmodel(models.Model):
    title=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.title}"
    
class intermediate_Languagemodel(models.Model):
    language_name=models.CharField(max_length=100,null=True)
    def  __str__(self):
        return f"{self.language_name}"