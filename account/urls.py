
from django.urls import path
from .import views as v

urlpatterns = [
    
    path("/adduser",v.adduser, name='add'),
    # add is a name of adduser in shortform
    path("/loginuser",v.loginuser,name='log'),
    path("/Logout",v.logot,name='logot'),
    path("/Search",v.srch,name="srch")
]
   
