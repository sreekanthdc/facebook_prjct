from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.myIndex, name='myIndex'),
    path('login/', views.checklogin),   
    path('register/', views.userRegistration),
    path('upload/', views.fileUpload, name="FileUpload"),
    path('adding/', views.addData, name="addData"),
    path('view/', views.viewProduct, name="viewProduct")
]
