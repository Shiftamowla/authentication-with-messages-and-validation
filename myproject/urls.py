from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('home/', home, name='home'),
    path('editSkill/<int:id>', editSkill, name='editSkill'),
    path('profilepage/', profilepage, name='profilepage'),
    path('listresume/', listresume, name='listresume'),
    path('addresume/', addresume, name='addresume'),
    path('currentresume/', currentresume, name='currentresume'),
    path('addSkill/', addSkill, name='addSkill'),
    path('addEducation/', addEducation, name='addEducation'),
    path('addExperience/', addExperience, name='addExperience'),
    path('addsInterest/', addsInterest, name='addsInterest'),
    path('addsLanguage/', addsLanguage, name='addsLanguage'),
    path('resume/<int:id>', resume, name='resume'),
    path('sdeletepage/<int:id>', sdeletepage, name='sdeletepage'),
    path('edeletepage/<int:id>', edeletepage, name='edeletepage'),
    path('ldeletepage/<int:id>', ldeletepage, name='ldeletepage'),
    path('exdeletepage/<int:id>', exdeletepage, name='exdeletepage'),
    path('ideletepage/<int:id>', ideletepage, name='ideletepage'),
    path('loginpage/', loginpage, name='loginpage'),
    path('registerpage/', registerpage, name='registerpage'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    path('skill_list/', skill_list, name='skill_list'),
    path('Education_list/', Education_list, name='Education_list'),
    path('Experience_list/', Experience_list, name='Experience_list'),
    path('Interest_list/', Interest_list, name='Interest_list'),
    path('Language_list/', Language_list, name='Language_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
