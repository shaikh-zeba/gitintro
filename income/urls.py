from django.urls import path
from . import  views as v

urlpatterns = [
      path("/Add",v.addincome,name="add"),
      path("/List",v.list,name="list"),
      #add income ko add ke naam se jana jayga
    #addincome 
   
]