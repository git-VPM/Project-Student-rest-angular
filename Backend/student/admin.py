from django.contrib import admin
from .models import Student, Dist

# Register your models here.

myModels = [Student, Dist]

admin.site.register(myModels)
