from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Authors)
admin.site.register(Publishers)
admin.site.register(SubjectClassification)
admin.site.register(Book)
admin.site.register(StudentExtra)
admin.site.register(IssuedBook)