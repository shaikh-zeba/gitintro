

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import IncomeModel

def addincome(request):
  if request.method=="POST":  
    amt=request.POST.get("amt")
    type=request.POST.get("type")
    date=request.POST.get("date")
    description=request.POST.get("description")
    uid=request.session.get("_auth_user_id")
    #it tsakes user id from auth_user
    #it takes id of 
    obj=User.objects.get(id=uid)


    obji=IncomeModel()
    obji.income_amount=amt
    obji.income_type=type
    obji.income_date=date
    obji.income_description=description
    obji.user=obj
    obji.save()
    return redirect("/")
  #for backtend

  else:
    print(request.session.items())
    return render(request,"incomeform.html")
  
  
  
def list(request):
  uid=request.session.get("_auth_user_id")
  obj=User.objects.get(id=uid)
  data=IncomeModel.objects.filter(user=obj)
  #use for some particular data u want filter
  d={
      "data":data
  }
  return render(request,"incdetails.html",d)
#for frontend
  
  
# Create your views here.
