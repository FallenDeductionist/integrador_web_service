from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alumno
from .serializers import AlumnoSerializer

# Create your views here.

# Lists all stocks or create a new one
# stocks/


class AlumnoList(APIView):

    def get(self, request):
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    def post(self):
        pass
