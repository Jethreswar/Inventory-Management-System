from django.shortcuts import get_object_or_404, redirect, render
from CRUDOpsByDjango.models import UserModel
from CRUDOpsByDjango.models import ProductDetailsModel
from CRUDOpsByDjango.models import ProductAudit
from django.contrib import messages

from datetime import datetime
def showDashboard(request):
    showall_users = UserModel.objects.all()
    return render(request, 'dashboard.html', {"data": showall_users})

def showDashboard2(request):
    showall_users = UserModel.objects.all()
    return render(request, 'dashboard.html', {"data": showall_users})

def showProducts(request):
    showall_products = ProductDetailsModel.objects.all()
    return render(request, 'index.html', {"data": showall_products})

def InsertUser(request):
    if request.method == "POST":
        if (request.POST.get("fname") and 
            request.POST.get("lname") and 
            request.POST.get("uname")):
            
            saverecord = UserModel()
            saverecord.fname = request.POST.get("fname")
            saverecord.lname = request.POST.get("lname")
            saverecord.uname = request.POST.get("uname")
            
            # Save the record to the database
            saverecord.save()

            messages.success(request, 'User registration ' + saverecord.fname + ' is saved successfully!')

    return render(request, 'new_user_register.html')

def InsertProductDetails(request,users_id):

    print("INTOOOOOOOOOO FOR INSERTION")
    user = UserModel.objects.get(users_id=users_id)
    if request.method == "POST":
        if (request.POST.get("pname") and 
            request.POST.get("desc") and 
            request.POST.get("stqty") and
            request.POST.get("price") ):
            #and request.POST.get("user") and
            #request.POST.get("products_id"))
            
            
            saverecord = ProductDetailsModel()
            saverecord.pname = request.POST.get("pname")
            #print("HELLLOOOOOOO",saverecord.pname)
            saverecord.desc = request.POST.get("desc")
            saverecord.stqty = int(request.POST.get("stqty"))
            saverecord.price = float(request.POST.get("price"))

            #saverecord.user = request.POST.get("user")
            #saverecord.products_id = request.POST.get("products_id")
            saverecord.user_id= user.uname
            #saverecord.products_id_id=1
            saverecord.save()
            foraudit = ProductAudit()
            #foraudit.id=saverecord.id
            foraudit.version=0
            foraudit.product=saverecord.id
            foraudit.name=saverecord.pname
            foraudit.qty=saverecord.stqty
            foraudit.price=saverecord.price
            foraudit.modifier=user.fname
            current_timestamp = datetime.now()
            foraudit.timestamp=current_timestamp
            foraudit.save()
            messages.success(request, 'Product details of ' + saverecord.pname + ' are saved successfully!')
    return render(request, 'insertproducts.html',{"user":user})

def EditProduct(request, id,users_id):
    user = UserModel.objects.get(users_id=users_id)
    print("Inside Editproduct view")
    print(user.uname)
    editproductobj = get_object_or_404(ProductDetailsModel, id=id)
    return render(request, 'Edit.html', {"ProductDetailsModel": editproductobj,"user":user})

def UpdateProducts(request, id,users_id):
    print("INTOOOOOO FOR UPDATE")
    user = UserModel.objects.get(users_id=users_id)
    print(user.uname)
    updateproduct = ProductDetailsModel.objects.get(id=id)
    print("NAME",updateproduct.pname)
    #form = Productforms(request.POST, instance=updateproduct)
    #if form.is_valid():
        #form.save()
    updateproduct.pname = request.POST.get("pname")
            #print("HELLLOOOOOOO",saverecord.pname)
    updateproduct.desc = request.POST.get("desc")
    updateproduct.stqty = int(request.POST.get("stqty"))
    updateproduct.price = float(request.POST.get("price"))
    updateproduct.save()
    forauditcount = ProductAudit.objects.filter(product=id)
    #finalauditcount=forauditcount-1
    finalauditcount=forauditcount.count()
    foraudit=ProductAudit()
    foraudit.version=finalauditcount
    foraudit.product=updateproduct.id
    foraudit.name=updateproduct.pname
    foraudit.qty=updateproduct.stqty
    foraudit.price=updateproduct.price
    foraudit.modifier=user.fname
    current_timestamp = datetime.now()
    foraudit.timestamp=current_timestamp
    foraudit.save()
    messages.success(request, 'Record updated successfully...!')
    return render(request, 'Edit.html', {"ProductDetailsModel": updateproduct,"user":user})

def DelProduct(request, id,users_id):
    user = UserModel.objects.get(users_id=users_id)
    delproduct = ProductDetailsModel.objects.get(id=id)
    delproduct.delete()
    showdata = ProductDetailsModel.objects.all()
    return render(request, 'index.html', {"data": showdata,"user":user})

def Phistory(request,id,users_id):
    print("FOR PRODUCT HISTORY")
    print("ID is", id)
    user = UserModel.objects.get(users_id=users_id)
    producthistory=ProductAudit.objects.filter(product=id)
    return render(request,"producthistory.html",{"Data":producthistory,"user":user})
    

def showProductDetails(request,users_id):
    print("TOOO SHOW")
    user = UserModel.objects.get(users_id=users_id)
    if request.method == 'POST':
        return redirect('index.html',{"user":user})
    return render(request, 'insertproducts.html')

def showProductDetails1(request,users_id):
    print("TOOO SHOW")
    user = UserModel.objects.get(users_id=users_id)
    if request.method == 'POST':
        return redirect('index.html',{"user":user})
    return render(request, 'insertproducts.html')

def addedProductDetails(request,users_id):
    user = UserModel.objects.get(users_id=users_id)
    print(user.uname)
    showall_products = ProductDetailsModel.objects.all()
    return render(request, 'index.html',{"data": showall_products,"user":user})