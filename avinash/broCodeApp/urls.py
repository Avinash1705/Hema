from django.contrib import admin
from django.urls import path
from broCodeApp import views

urlpatterns = [
    path("", views.index,name='broCodeApp'),

    path("createSuperDistributer", views.createSuperDistributer,name='broCodeApp'),

    path("createDistributer", views.createDistributer,name='broCodeApp'),

    path("createRetailer", views.createRetailer,name='broCodeApp'),

    path("editUser", views.editUser,name='broCodeApp'),

    path("editWlCouponMargin", views.    ,name='broCodeApp'),

    path("home", views.home,name='broCodeApp'),
    
    path("joiningList",views.joiningList,name='broCodeApp'),

    # Coupon Req
    path("retailerCouponReq",views.retailerCouponReq,name='broCodeApp'),

    path("distributePCoupon",views.distributePCoupon,name='broCodeApp'),

    path("distributeECoupon",views.distributeECoupon,name='broCodeApp'),

    path("deductUserCoupon",views.deductUserCoupon,name='broCodeApp'),

    path("retailerCouponSummary",views.retailerCouponSummary,name='broCodeApp'),

    path("retailerOnlineCouponSummary",views.retailerOnlineCouponSummary,name='broCodeApp'),

    path("markRetailerAsRestricted",views.markRetailerAsRestricted,name='broCodeApp'),

    path("unMarkRetailerAsRestricted",views.unMarkRetailerAsRestricted,name='broCodeApp'),

    # settings
    path("aDDEmploye",views.aDDEmploye,name='broCodeApp'),
    path("orderIdVerify",views.orderIdVerify,name='broCodeApp'),
    path("resetMasterPassword",views.resetMasterPassword,name='broCodeApp'),
    path("changeUserMargin",views.changeUserMargin,name='broCodeApp'),
    path("searchById",views.searchById,name='broCodeApp'),

    # lb Users
    path("sessionUpdate",views.unMarkRetailerAsRestricted,name='broCodeApp'),
    path("lbUsers",views.unMarkRetailerAsRestricted,name='broCodeApp'),
    path("unMarkRetailerAsRestricted",views.unMarkRetailerAsRestricted,name='broCodeApp')

]