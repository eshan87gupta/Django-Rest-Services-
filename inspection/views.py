from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView)

from .models import SchoolSelfies, SchoolMaster, surveyor_registration, HRTeachers, InfrastructureDetails, Students, TeachingQuality, MidDayMealQuality, MDMDataDetails, MDMData
from .picsSerializer.serializer import SchoolSelfiesSerializer
from .school_master.serializer import SchoolMasterSerializer
from .registration.serializer import SurveyorRegistrationSerializer
from .hrteacher.serializer import HRTeacherSerializer
from .infradetails.serializer import InfrastructureSerializer
from .studentsdetails.serializer import StudentSerializer
from .teachingQualityDetails.serializer import TeachingQualitySerializer
from .middaymealdetails.serializer import MidDayMealSerializer
from .agencyDetails.serializer import AgencyDetailsSerializer
from .mdmdata.serializer import MDMDataSerializer


class SchoolImages(APIView):
    def get(self, request):
        coords = SchoolSelfies.object.all()
        serializer = SchoolSelfiesSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = SchoolSelfiesSerializer(data=request.data)
        print(coords.is_valid())
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


class MDMDataBase(APIView):
    def get(self, request):
        coords = MDMData.object.all()
        serializer = MDMDataSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = MDMDataSerializer(data=request.data)
        print(coords.is_valid())
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


class AgencyDetails(APIView):
    def get(self, request):
        coords = MDMDataDetails.object.all()
        serializer = AgencyDetailsSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = AgencyDetailsSerializer(data=request.data)
        print(coords.is_valid())
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)



class MidDay(APIView):
    def get(self, request):
        coords = MidDayMealQuality.object.all()
        serializer = MidDayMealSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = MidDayMealSerializer(data=request.data)
        print(coords.is_valid())
        name = request.data["school_name"]
        print(name)
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)



class Teaching(APIView):
    def get(self, request):
        coords = TeachingQuality.object.all()
        serializer = TeachingQualitySerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = TeachingQualitySerializer(data=request.data)
        print(coords.is_valid())
        name = request.data["school_name"]
        print(name)
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentData(APIView):
    def get(self, request):
        coords = Students.object.all()
        serializer = StudentSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = StudentSerializer(data=request.data)
        print(coords.is_valid())
        name = request.data["school_name"]
        print(name)
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


class Infrastructure(APIView):
    def get(self, request):
        coords = InfrastructureDetails.object.all()
        serializer = InfrastructureSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = InfrastructureSerializer(data=request.data)
        print(coords.is_valid())
        name = request.data["school_name"]
        print(name)
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


class Teacher(APIView):
    def get(self, request):
        coords = HRTeachers.object.all()
        serializer = HRTeacherSerializer(coords, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = HRTeacherSerializer(data=request.data)
        print(coords.is_valid())
        name = request.data["teacher_name"]
        print(name)
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


class LoadData(APIView):
    def get(self, request):
        dataSch = SchoolMaster.object.all()
        print(len(dataSch))
        dataSch = dataSch[98543:100345]
        print(len(dataSch))
        serializer = SchoolMasterSerializer(dataSch, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = SchoolMasterSerializer(data=request.data)
        print(coords.is_valid())
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


class Registration(APIView):
    def get(self, request):
        dataSch = surveyor_registration.object.all()
        serializer = SurveyorRegistrationSerializer(dataSch, many=True)
        return Response(serializer.data)

    def post(self, request):
        coords = SurveyorRegistrationSerializer(data=request.data)
        print(coords.is_valid())
        # name = request.data["surveyor_name"]
        # desig = request.data["surveyor_designation"]
        # mobile = request.data["mobile"]
        # surveyor_registration(surveyor_name=name, surveyor_designation=desig, mobile=mobile).save()
        print("yes, its done")
        if coords.is_valid():
            coords.save()
            return Response(coords.data, status=status.HTTP_201_CREATED)
        return Response(coords.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
