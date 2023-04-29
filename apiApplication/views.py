from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import *
class PersonalProfileApiView(APIView):


    def get(self, request, format=None):
        personal_profile=PersonalProfile.objects.all().values()
        return Response ({"Personal Profile Details:": personal_profile})

    def post(self, request, format=None):
        PersonalProfile.objects.create(id=request.data["id"],
                                       name=request.data["name"],
                                       intro=request.data["intro"],
                                       phone=request.data["phone"],
                                       email =request.data["email"],
                                       birthdate=request.data["birthdate"],
                                       linkedin=request.data["linkedin"],

                                       )
        personal_profile = PersonalProfile.objects.all().values()
        return Response({"Personal Profile Details:": personal_profile})


class EducationApiView(APIView):

    def get(self, request, format=None):
        education=Education.objects.all().values()
        return Response({"Education Details:": education})

    def post(self, request, format=None):
        Education.objects.create(id=request.data["id"],
                                       name=request.data["name"],
                                       title=request.data["title"],
                                       desciption=request.data["desciption"],


                                       )
        education=Education.objects.all().values()
        return Response({"education Details:": education})


class ProfessionalExperienceApiView(APIView):

    def get(self, request, format=None):
        experience= ProfessionalExperience.objects.all().values()
        return Response({"professional experience Details:": experience})

    def post(self, request, format=None):
        ProfessionalExperience.objects.create(id=request.data["id"],
                                 name=request.data["name"],
                                 title=request.data["title"],
                                 header=request.data["header"],
                                 desciption=request.data["desciption"],


                                 )
        experience= ProfessionalExperience.objects.all().values()
        return Response({"experience Details:": experience})


class AcademicProjectsApiView(APIView):

    def get(self, request, format=None):
        projects= AcademicProjects.objects.all().values()
        return Response({"academic projects Details:": projects})

    def post(self, request, format=None):
        AcademicProjects.objects.create(id=request.data["id"],
                                 name=request.data["name"],
                                 title=request.data["title"],
                                 desciption=request.data["desciption"],

                                 )
        projects= AcademicProjects.objects.all().values()
        return Response({"projectsD details:": projects})
class AssociativeLifeApiView(APIView):

    def get(self, request, format=None):
        associative= AssociativeLife.objects.all().values()
        return Response({"associative life Details:": associative})
    def post(self, request, format=None):
        AssociativeLife.objects.create(id=request.data["id"],
                                 name=request.data["name"],
                                 title=request.data["title"],
                                 desciption=request.data["desciption"],

                                 )
        associative= AssociativeLife.objects.all().values()
        return Response({"associative details:": associative})
class SkillsApiView(APIView):

    def get(self, request, format=None):
        skills= Skills.objects.all().values()
        return Response({"skills Details:": skills})

    def post(self, request, format=None):
        Skills.objects.create(id=request.data["id"],
                                 name=request.data["name"],
                                 title=request.data["title"],
                                 desciption=request.data["desciption"],

                                 )
        skills= Skills.objects.all().values()
        return Response({"skills details:": skills})

class CertficatesApiView(APIView):

    def get(self, request, format=None):
        certficates= Certficates.objects.all().values()
        return Response({"certficates  Details:": certficates})

    def post(self, request, format=None):
        Certficates.objects.create(id=request.data["id"],
                                 name=request.data["name"],
                                 title=request.data["title"],
                                 desciption=request.data["desciption"],

                                 )
        certficates= Certficates.objects.all().values()
        return Response({"certficates etails:": certficates})
class LanguagesApiView(APIView):
     def get(self, request, format=None):
        languages= Languages.objects.all().values()
        return Response({"languages  Details:": languages})

     def post(self, request, format=None):
        Languages.objects.create(id=request.data["id"],
                                 name=request.data["name"],
                                 title=request.data["title"],

                                 )
        languages= Languages.objects.all().values()
        return Response({"languages  details:": languages})