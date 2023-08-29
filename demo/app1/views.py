from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .serailizer import EmployeeSerializer


# Create your views here.

def home(request):
    return render(request,'home.html')


class EmployeeDetail(APIView):
    def get(self, request):
        obj = Employee.objects.all()
        serialzier = EmployeeSerializer(obj, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfo(APIView):
    def get(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg": "not found error"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serialzier = EmployeeSerializer(obj, data=request.data)

        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg": "not found error"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serialzier = EmployeeSerializer(obj, data=request.data, partial=True)

        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)
