# from django.shortcuts import render
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status

# from student.models import Student
# from student.serializers import StudentSerializer
# from rest_framework.decorators import api_view


# @api_view(['GET', 'POST', 'DELETE'])
# def student_list(request):
#     # GET list of students, POST a new one, DELETE all

#     # Retrieve all students/ find by name from PostgreSQL database:
#     if request.method == 'GET':
#         students = Student.objects.all()

#         name = request.GET.get('name', None)
#         if name is not None:
#             students = students.filter(title__icontains=name)

#         students_serializer = StudentSerializer(students, many=True)
#         return JsonResponse(students_serializer.data, safe=False)
#         # 'safe=False' for objects serialization

#     # Create and Save a new Student:
#     elif request.method == 'POST':
#         students_data = JSONParser().parse(request)
#         students_serializer = StudentSerializer(data=students_data)
#         if students_serializer.is_valid():
#             students_serializer.save()
#             return JsonResponse(students_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(students_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete all Students from the database:
#     elif request.method == 'DELETE':
#         count = Student.objects.all().delete()
#         return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk):
#     # find student by pk (id)
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     # GET / PUT / DELETE student
#     # Find a single Student with an id:
#     if request.method == 'GET':
#         students_serializer = StudentSerializer(student)
#         return JsonResponse(students_serializer.data)

#     # Update a Student by the id in the request:
#     elif request.method == 'PUT':
#         student_data = JSONParser().parse(request)
#         students_serializer = StudentSerializer(student, data=student_data)
#         if students_serializer.is_valid():
#             students_serializer.save()
#             return JsonResponse(students_serializer.data)
#         return JsonResponse(students_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete a Student with the specified id:
#     elif request.method == 'DELETE':
#         student.delete()
#         return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# # @api_view(['GET'])
# # def student_list_published(request):
# #     # GET all published students
# #     # Find all Students with published = True:
# #     students = Student.objects.filter(published=True)

# #     if request.method == 'GET':
# #         students_serializer = StudentSerializer(students, many=True)
# #         return JsonResponse(students_serializer.data, safe=False)


from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import APIView
from . models import Student, Dist
from . serializers import StudentSerializer, DistSerializer
from rest_framework.response import Response


class getprofile_by_id(APIView):
    # to show student data by id by using / after url in Django REST framework
    def get(self, requests, key):
        takepro = Student.objects.get(id=key)
        takeallpro = StudentSerializer(takepro)
        return Response(takeallpro.data)

    def put(self, requests, key):
        # to replace/update student data
        takepro = Student.objects.get(id=key)
        takeallpro = StudentSerializer(takepro, requests.data)
        if takeallpro.is_valid():
            takeallpro.save()
            return Response(takeallpro.data)
        else:
            return Response('No data added')

    def delete(self, requests, key):
        # to delete student data
        takepro = Student.objects.get(id=key)
        takepro.delete()
        return Response('Student data removed')


class getprofile(APIView):
    def get(self, requests):
        takepro = Student.objects.all()
        takeallpro = StudentSerializer(takepro, many=True)
        return Response(takeallpro.data)

    def post(self, requests):
        # to add a new student data
        takeallpro = StudentSerializer(data=requests.data)
        if takeallpro.is_valid():
            takeallpro.save()
            return Response({'status': 1, 'data': takeallpro.data})
        else:
            return Response({'status': 0, 'msg': 'The submitted Data is invalid'})

    def delete(self, requests):
        # to delete student data
        takepro = Student.objects.all()
        takepro.delete()
        return Response('All student data removed')


class getdist(APIView):
    # to get dist
    def get(self, requests):
        # import pdb
        # pdb.set_trace()
        takepro = Dist.objects.all()
        takeallpro = DistSerializer(takepro, many=True)
        return Response(takeallpro.data)


class get_by_id(APIView):
    # to show dist data by id by using / after url in Django REST framework
    def get(self, requests, key):
        takepro = Dist.objects.get(pk_bint_id=key)
        takeallpro = DistSerializer(takepro)
        return Response(takeallpro.data)

    # def student_list(request):
    #     # Retrieve all Tutorials/ find by name from PostgreSQL database:
    #     students = Student.objects.all()
    #     name = request.GET.get('name', None)
    #     if name is not None:
    #         students = students.filter(name__icontains=name)

    #     students_serializer = StudentSerializer(students, many=True)
    #     return Response(students_serializer.data)
