from django.contrib import admin
from django.urls import path
from django.urls import re_path
from apiApplication import  views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("profile/", views.PersonalProfileApiView.as_view()),
    re_path("education/", views.EducationApiView.as_view()),
    re_path("experience/", views.ProfessionalExperienceApiView.as_view()),
    re_path("academicProjects/", views.AcademicProjectsApiView.as_view()),
    re_path("associativeLife/", views.AssociativeLifeApiView.as_view()),
    re_path("skills/", views.SkillsApiView.as_view()),
    re_path("certficates/", views.CertficatesApiView.as_view()),
    re_path("languages/", views.LanguagesApiView.as_view()),

]
