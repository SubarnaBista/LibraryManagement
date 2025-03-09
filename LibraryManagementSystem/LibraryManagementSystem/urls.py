"""
URL configuration for LibraryManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('adminclicked',views.adminclickedview,name='adminview'),
    path('adminlogin',views.adminloginview,name='adminlogin'),
    path('adminhome',views.adminloginview,name='adminhome'),
    path('addbook',views.addbookview,name='addbook'),
    path('booksview',views.bookdetailsview,name='bookview'),
    path('booksview/<int:id>',views.deletebookview,name='delbookview'),
    path('confirmdelete/<str:model>/<int:id>/', views.confirmdeleteview, name='confirmdelete'),
    path('',views.homepage,name='index'),
    path('admindash',views.admindashboard,name='admindash'),
    path('Managebook',views.managebookview,name='managebook'),
    path('author',views.authordetailsview,name='author'),
    path('author/<int:id>',views.deleteauthorview,name='delauthor'),
    path('addauthor',views.addauthorview,name='addauthor'),
    path('publisher',views.publisherview,name='publisher'),
    path('addpublisher',views.addpublisherview,name='addpublisher'),
    path('publisher/<int:id>',views.deletepublishers,name='delpublisher'),
    path('logout',views.logoutview,name='logout'),
    path('studentsignup/', views.studentsignup_view, name='studentsignup'),
    path('studentlogin/', views.studentloginview, name='studentlogin'),
    path('studenthome/', views.studenthomeview, name='studenthomes'),
    path('viewstudent', views.viewstudents,name='studentview'),
    path('issuebook', views.issuebookview,name='issuebook'),
    path('viewissuedbook',views.issuedbooksdetail,name='viewissuedbook'),
    path('issuedfulldetails',views.issuedfulldetails,name='issuedfulldetails'),
    path('studentsbookv',views.viewbooksstudent,name='studentsbookv'),
    path('bookissuedtostudent',views.bookissuedtostudent,name='bookissuedtostudent'),
]
