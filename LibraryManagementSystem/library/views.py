from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from . import forms
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
def homepage(request):
    # return HttpResponse("i am don")
    return render(request,'index.html')


def adminclickedview(request):
    return render(request,'adminclicked.html')


def adminloginview(request):
    if request.method == "POST":
        username=request.POST['username1']
        password=request.POST['pass1']


        user=authenticate(username=username,password=password)
         
        if user is not None : #check authentication was successfull or not
              if user.is_superuser or user.is_staff:
                login(request,user)
                helloadmin=user.username
                # return redirect("admindash.html",{'helloadmin':helloadmin})
                return redirect('admindash')
              else:
                  messages.error(request,"bad credientals")

        else:
          messages.error(request,"bad credientals")
          

    return render(request,'adminlogin.html')
@login_required(login_url='adminlogin')
def addbookview(request):
    # Fetch all authors, publishers, and categories from the database
    authors = Authors.objects.all()
    publishers = Publishers.objects.all()

    if request.method == 'POST':
        # Get the data from the form submission
        bookname = request.POST.get('bookname')
        author_id = request.POST.get('author')
        publisher_id = request.POST.get('publication')
        details=request.POST['bookdetails']

        # Fetch the related author, publisher, and category objects using the IDs
        author = Authors.objects.get(id=author_id)
        publisher = Publishers.objects.get(id=publisher_id)

        # Create a new Book entry
        new_book = Book(
            name=bookname,
            author=author,
            publisher=publisher,
            details=details
        )
        new_book.save()  
        messages.success(request,"Books added SuccessFully")

      
        return redirect('bookview')  
    return render(request, 'addbook.html', {'author': authors, 'publisher': publishers})

def bookdetailsview(request):
    books=Book.objects.all()
    return render(request,'booksview.html',{'books':books})
@login_required(login_url='adminlogin')
def managebookview(request):
    return render(request,"managebook.html")

@login_required(login_url='adminlogin')
def publisherview(request):
    datas=Publishers.objects.all()
    if request.method == "POST":
        name=request.POST['publishername']
        details=request.POST['publisherdetails']
        publisherdata=Publishers(name=name,details=details)
        publisherdata.save()
        messages.success(request,"added successfully")    
        

    return render(request,"publisherdetails.html",{'pub':datas})

@login_required(login_url='adminlogin')
def addpublisherview(request):
    if request.method == "POST":
        name=request.POST['publishername']
        details=request.POST['publisherdetails']
        publisherdata=Publishers(name=name,details=details)
        publisherdata.save()
        messages.success(request,"added successfully")
        return redirect('publisher')
    return render(request,"addpublisher.html")

@login_required(login_url='adminlogin')
def deletepublishers(request,id):
    delit=Publishers.objects.get(id=id)
    delit.delete()
    messages.success(request,"deleted successfully" )
    return redirect('publisher')
@login_required(login_url='adminlogin')
def authordetailsview(request):
    authordata=Authors.objects.all()
    if request.method == "POST":
        name1=request.POST['authorname']
        details1=request.POST['authordetails']
        authordata=Authors(name=name1,details=details1)
        authordata.save()
        messages.success(request,"Author Added Successfully")
        return redirect('author')
    return render(request,'authordetails.html',{"authordata":authordata})
@login_required(login_url='adminlogin')
def addauthorview(request):
    return render(request,"addauthor.html")
@login_required(login_url='adminlogin')
def deleteauthorview(request,id):
    delauthor=Authors.objects.get(id=id)
    delauthor.delete()
    messages.success(request,"Author deleted successfully")
    return redirect('author')
@login_required(login_url='adminlogin')
def deletebookview(request,id):
    delitbook=Book.objects.get(id=id)
    delitbook.delete()
    # messages.success(request,"Book deleted Successfully")
    return redirect('bookview')
@login_required(login_url='adminlogin')
def admindashboard(request):
    uname=request.user.username
    return render(request,"admindash.html",{"uname":uname})
def logoutview(request):
    logout(request)
    # messages.success(request,"logout successfully")
    return redirect('index')

@login_required(login_url='adminlogin')
def confirmdeleteview(request, id, model):
    if model == 'book':
        instance = Book.objects.get(id=id)
        model_name = 'Book'
    elif model == 'author':
        instance = Authors.objects.get(id=id)
        model_name = 'Author'
    elif model == 'publisher':
        instance = Publishers.objects.get(id=id)
        model_name = 'Publisher'
    else:
        messages.error(request, "Invalid model")
        return redirect('bookview')  

    # If the request method is POST, delete the object
    if request.method == "POST":
        instance.delete()
        messages.success(request, f"{model_name} Deleted Successfully")
        
        # Redirect to the appropriate view after deletion
        if model == 'book':
            return redirect('bookview')
        elif model == 'author':
            return redirect('author')
        elif model == 'publisher':
            return redirect('publisher')

    # Render the confirmation page with the model data
    return render(request, 'confirmdelete.html', {"instance": instance, "model_name": model_name})


def studentsignup_view(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)

        return redirect('studentlogin')
    return render(request,'studentsignup.html',context=mydict)

def studentloginview(request):
    if request.method == 'POST':
        username=request.POST['username1']
        password=request.POST['pass1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name='STUDENT').exists():
                login(request, user)
                return redirect('studenthomes')
            else:
                # If user does not belong to "STUDENT" group, show error message
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
   
    
    return render(request, 'studentlogin.html')


@login_required(login_url='studentlogin')
def studenthomeview(request):
    return render(request,'studenthome.html')

@login_required(login_url='adminlogin')
def viewstudents(request):
    students=StudentExtra.objects.all()
    return render(request,"viewstudent.html",{"students":students})
def isadminuser(user):
    if user.is_superuser or user.is_staff:
        return True
    else:
        return False

@login_required(login_url='adminlogin')
@user_passes_test(isadminuser)
def issuebookview(request):
    if request.method == 'POST':
        # Get the selected book and student IDs from the form
        book_id = request.POST.get('book')
        student_id = request.POST.get('issuedstudentname')

        # Retrieve the Book and Student objects
        book = Book.objects.get(id=book_id)
        book.issued=True
        book.save()
        student = StudentExtra.objects.get(id=student_id)

        # Create a new IssuedBook instance and save it
        issued_book = IssuedBook(
            bookname=book,
            studentname=student
        )
        issued_book.save()
        messages.success(request,"Book issued successfully")

        # Redirect or render a success message
        return redirect('viewissuedbook')  
    else:
        # Load the books and students for the form
        bookdetail = Book.objects.filter(issued=False)
        studentdetails = StudentExtra.objects.all()
        return render(request, 'issuebook.html', {
            'bookdetail': bookdetail,
            'studentdetails': studentdetails,
        })
@user_passes_test(isadminuser)
def issuedbooksdetail(request):
    return render(request,'issuedbookview.html')
@user_passes_test(isadminuser)
def issuedfulldetails(request):
    details=IssuedBook.objects.all()
    return render(request,'issuedfulldetails.html',{'details':details})
@login_required 
def viewbooksstudent(request):
    books=Book.objects.filter(issued=False)
    return render(request,'viewbooksstudent.html',{'books':books})
@login_required 
def bookissuedtostudent(request):
    student = request.user.studentextra
    issued_books = IssuedBook.objects.filter(studentname=student)

    return render(request,'bookissuedtostudent.html',{'issued_books': issued_books})