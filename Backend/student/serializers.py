from .models import Student, Dist
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class DistSerializer(ModelSerializer):

    class Meta:
        model = Dist
        fields = '__all__'
