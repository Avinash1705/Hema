from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is DashBoard")
    context ={
        "MyAvinash" :"this is send from views for Avinash ",
        "MyHema" :"this is send from views for Hemma"
      }
    return render(request,'index.html',context)
    
def home(request):
        # return HttpResponse("Home page")
        return render(request,'home.html')
def joiningList(request):

   return render (request , 'joiningList.html')

def createSuperDistributer(request):
    # return HttpResponse("createSuperDistributer")
   return render (request , 'createSuperDistributer.html')

    
def createDistributer(request):
    # return HttpResponse("createSuperDistributer")
   return render (request , 'createDistributer.html')


def createRetailer(request):
    # return HttpResponse("createSuperDistributer")
   return render (request , 'createRetailer.html')


def editUser(request):
    return render(request,"editUser.html")

def editWLAccountCreationCouponMargin(request):
    # return HttpResponse("createSuperDistributer")
   return render (request , 'editWlCouponMargin.html')

# Retailer Coupon Nav
def retailerCouponReq(request):
   return render (request , 'RetailerCouponReq.html')

def distributePCoupon(request):
   return render (request , 'distributePCoupon.html')
def distributeECoupon(request):
   return render (request , 'distributeECoupon.html')
def distributePCoupon(request):
   return render (request , 'distributePCoupon.html')
def deductUserCoupon(request):
   return render (request , 'deductUserCoupon.html')
def retailerCouponSummary(request):
    return render(request,'retailerCouponSummary.html')
def retailerOnlineCouponSummary(request):
   return render (request , 'retailerOnlineCouponSummary.html')
def markRetailerAsRestricted(request):
   return render (request , 'markRetailerAsRestricted.html')
def unMarkRetailerAsRestricted(request):
   return render (request , 'unMarkRetailerAsRestricted.html')

def aDDEmploye(request):
    return render(request, 'aDeacticateDelete.html')
def orderIdVerify(request):
    return render(request, 'orderIdVerify.html')
def resetMasterPassword(request):
    return render(request, 'resetMasterPassword.html')
def changeUserMargin(request):
    return render(request, 'changeUserMargin.html')
def searchById(request):
    return render(request, 'searchById.html')