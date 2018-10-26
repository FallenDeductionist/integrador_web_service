from rest_framework import serializers
from .models import Alumno
from .models import Resultado


class ResultadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resultado
        fields = 'empresa', 'tiempo', 'comentarios'


class AlumnoSerializer(serializers.ModelSerializer):
    resultado = ResultadoSerializer(many=True, read_only=True)

    class Meta:
        model = Alumno
        fields = 'nombre', 'apellido', 'email', 'resultado'
