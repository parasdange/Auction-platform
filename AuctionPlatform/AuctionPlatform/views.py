from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .models import UserInfo

from django.contrib.auth.hashers import make_password

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from  django.contrib.auth.decorators import login_required

from seller.models import Product,Product_images

from seller.models import City,Category

from bidder.models import Bidder_product

def login_call(request):

	if request.method=="POST":
		un=request.POST["username"]
		up=request.POST["pass"]

		user=authenticate(username=un,password=up)

		if user:

			uobj=User.objects.get(username=un)


			login(request,user)

			if uobj.is_superuser==1:

				return redirect('/admin_user/')



			return redirect("/userdashboard/")

		else:
			messages.error(request,"Error! Please enter valid Username and Password.")


			

	return render(request,"login.html")

@login_required
def userdashboard(request):

	pobj=Product.objects.all()
	bobj=Bidder_product.objects.all()

	wobj=[]

	for i in pobj:
		for j in bobj:
			if(i.id==j.product_id):
				if j.status==1:
					wobj.append(i)

	remain_pobj=[]

	for i in pobj:
		if i not in wobj: 
			remain_pobj.append(i)

	sobj=Bidder_product.objects.filter(place_status=1)

	s_obj=[]

	for i in sobj:

		obj=Product.objects.get(id=i.product_id)
		obj.final_price=i.bid_amount

		s_obj.append(obj)		


	return render(request,"userdashboard.html",{'pobj':remain_pobj,'sobj':s_obj})
	

		

			

@login_required
def logout_call(request):
	logout(request)
	return redirect("/home/")


def signup(request):

	


	if request.method=="POST":
		fn=request.POST["first_name"]
		ln=request.POST["last_name"]
		un=request.POST["user_name"]
		pwd=request.POST["password"]
		email=request.POST["email"]
		address=request.POST["address"]
		mob=request.POST["mob"]

		uobj=User(first_name=fn,last_name=ln,username=un,password=make_password(pwd),email=email)
		uobj.save()

		UserInfo_obj=UserInfo(mobile=mob,address=address,user=uobj,password=pwd)
		UserInfo_obj.save()

		messages.success(request,"Success! Account Created Successfully. Please Login Now.")
		return redirect("/login/")

	return render(request,"signup.html")

def home(request):

	p_obj=Product.objects.all()
	bobj=Bidder_product.objects.all()

	wobj=[]

	for i in p_obj:
		for j in bobj:
			if(i.id==j.product_id):
				if j.status==1:
					wobj.append(i)

	remain_pobj=[]

	for i in p_obj:
		if i not in wobj: 
			remain_pobj.append(i)


	sobj=Bidder_product.objects.filter(place_status=1)

	s_obj=[]

	for i in sobj:

		pobj=Product.objects.get(id=i.product_id)
		pobj.final_price=i.bid_amount

		s_obj.append(pobj)



	# print(p_obj)

	
	# closing_date=[]

	# for i in p_obj:
	# 	date=i.closing_date.split("-")
	# 	date1=[]
	# 	for i in range(1,len(date)+1):
	# 		date1.append(date[-i])


	# 	ndate=":".join(date1)
	# 	closing_date.append(ndate)

		
	# # for i in p_obj:

	# # 	print(i.closing_date)
	# 	# print(type(i.closing_date))
	# print(closing_date)	

	return render(request,"home.html",{'pobj':remain_pobj,'sobj':s_obj})

@login_required

def admin_user(request):

	return render(request,'admin.html')


def add_category(request):

	if request.method == "POST":
		cat=request.POST["add_cat"]

		cobj=Category(catname=cat)
		cobj.save()

		messages.success(request,' Category added Successfully .')
	return render(request,'add_category.html')



def categories_list(request):

	cobj=Category.objects.all()

	s=1
	for i in cobj:
		i.s_no=s
		s=s+1

	return render(request,'categories_list.html',{'cobj':cobj})


















