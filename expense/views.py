

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import ExpenseModel

def addexpense(request):
  if request.method=="POST":  
    amt=request.POST.get("amt")
    type=request.POST.get("type")
    date=request.POST.get("date")
    description=request.POST.get("description")
    uid=request.session.get("_auth_user_id")
    #it takes auth-user id
    obj=User.objects.get(id=uid)


    obji=ExpenseModel()
    # use model from model
    obji.expense_amount=amt
    obji.expense_type=type
    obji.expense_date=date
    obji.expense_description=description
    obji.user=obj
    obji.save()
    return redirect("/")

  else:
    return render(request,"expenseform.html")

  
def list(request):
  uid=request.session.get("_auth_user_id")
  obj=User.objects.get(id=uid)
  data=ExpenseModel.objects.filter(user=obj)
  #use for some particular data want
  #u use filter u see only login person explist and  inclist
  d={
    "data":data
  }
  return render(request,"expdetails.html",d)
  



# Create your views here.

