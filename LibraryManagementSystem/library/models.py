from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import datetime,timedelta

# Create your models here.
class Authors(models.Model):
    name=models.TextField(max_length=30)
    details=models.TextField(max_length=200)

    def __str__(self):
         return self.name

    

class Publishers(models.Model):
     name=models.TextField(max_length=30)
     details=models.TextField(max_length=200)

     def __str__(self):
         return self.name

class SubjectClassification(models.Model):
     name=models.TextField(max_length=30)
     def __str__(self):
         return self.name

class Book(models.Model):
     name=models.CharField(max_length=30)
     author=models.ForeignKey(Authors, on_delete=models.CASCADE)
     publisher=models.ForeignKey(Publishers, on_delete=models.CASCADE)
     category=models.ForeignKey(SubjectClassification, on_delete=models.CASCADE, null=True,blank=True)
     details=models.CharField(max_length=300,default="hello this is book")
     issued=models.BooleanField(default=False)
     def __str__(self):
          return self.name

                
class StudentUser(AbstractUser):
    is_student = models.BooleanField(default=True)
    student_id = models.CharField(max_length=10, unique=True)

    # Explicitly defining related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='studentuser_set',  # Change reverse access name for groups
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='studentuser_permissions',  
        blank=True
    )

    def __str__(self):
        return self.username

class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    section = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id
    
def get_expiry():
    return datetime.today() + timedelta(days=20)
class IssuedBook(models.Model):
    studentname = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
    bookname = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Book {self.bookname.name}"