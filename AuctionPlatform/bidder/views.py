
import datetime

from django.contrib.auth.hashers import make_password

from django.shortcuts import render,redirect

from seller.models import Product,Product_images,Category

from django.contrib.auth.models import User

from django.contrib import messages

from AuctionPlatform.models import UserInfo 

from django.contrib.auth import authenticate,login,logout

from . models import Bidder_product,Pyment_method,Orders

import random

import datetime
# Create your views here.

def viewproduct(request,id):

	pobj=Product.objects.get(id=id)
	p_img=Product_images.objects.filter(product=id)

	u_obj=User.objects.get(username=pobj.added_by)
	u_name=u_obj.first_name+" "+u_obj.last_name

	close_date=pobj.closing_date.split(":")
	# print(close_date)

	january1st = datetime.datetime(int(close_date[2]),int(close_date[1]),int(close_date[0]))
	# january1st = datetime.datetime(2021,6,21)
	timesince =  january1st-datetime.datetime.now()
	minutessince = int(timesince.total_seconds() / 60)

	# current_date_arr=[]

	# c_date=datetime.datetime.now()

	# current_date_arr.append(c_date.strftime("%d"))
	# current_date_arr.append(c_date.strftime("%m"))
	# current_date_arr.append(str(c_date.year))

	# if(current_date_arr==close_date):
	# 	timesince =  datetime.datetime.now()- january1st
	# 	minutessince = int(timesince.total_seconds() / 60)
		
	remaning_hour=int(minutessince/60)

	# print(remaning_hour)
	
	close_date="-".join(close_date)

	current_user=User.objects.get(username=request.user)

	current_user_bid_obj=Bidder_product.objects.filter(bid_by=current_user.id)

	# bid_item=Bidder_product.objects.filter(product_id=id)

	# ord_obj=Orders.objects.filter(bid_id=bid_item.id)

	# for i in ord_obj:
	# 	if ord_obj.bid_id==bid_item.id:
	# 		messages.success(request,"Order placed Successfully.")
	# 		return render(request,"viewproduct.html",{'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})
		
	  		
	 		

	for i in current_user_bid_obj:

		if (i.product_id==id):

			if (i.status == 1):

	 			messages.success(request,"Congratulation You win the product.")

	 			return render(request,"viewproduct.html",{'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})
	 		# if i.place_status == 1:
	 		# 	messages.success(request,"Order placed Successfully.")
	 		# 	return render(request,"viewproduct.html",{'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})

	 			
	 			
	 			

	 		
	 			

	 			

	 			


	
			
			

	if(current_user.id==pobj.added_by_id):
		messages.error(request,"You can not bid on  your own products.")

	
	if request.method=="POST":
	 	bid_amount=request.POST["bid_amount"]

	 	bobj=Bidder_product(product=pobj,bid_by=current_user,bid_amount=bid_amount)
	 	bobj.save()

	 	messages.success(request," You have bid on this product successfully.")


	 	return render(request,"bid_product.html",{'bidding_amount':bid_amount,'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})


	bidding_obj=Bidder_product.objects.filter(bid_by=current_user.id)

	for i in bidding_obj:
		if i.product_id == id:
			return render(request,"bid_product.html",{'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})


	return render(request,"viewproduct.html",{'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})




# def bid_product(request,id):
# 	pobj=Product.objects.get(id=id)
# 	p_img=Product_images.objects.filter(product=id)

# 	u_obj=User.objects.get(username=pobj.added_by)
# 	u_name=u_obj.first_name+" "+u_obj.last_name

# 	close_date=pobj.closing_date.split(":")
	

# 	january1st = datetime.datetime(int(close_date[2]),int(close_date[1]),int(close_date[0]))
	
# 	timesince =  january1st-datetime.datetime.now()
# 	minutessince = int(timesince.total_seconds() / 60)

	
		
# 	remaning_hour=int(minutessince/60)

	
	
# 	close_date="-".join(close_date)

# 	current_user=User.objects.get(username=request.user)

	

	

	
# 	if request.method=="POST":
# 		bid_amount=request.POST["bid_amount"]

# 		bobj=Bidder_product(product=pobj,bid_by=current_user,bid_amount=bid_amount)
# 		bobj.save()

# 		messages.success(request," You have bid on this product successfully.")

# 	bidding_obj=Bidder_product.objects.filter(bid_by=current_user.id)

# 	bidding_amount=0;

# 	for i in bidding_obj:

# 		if i.product_id == id:

# 			bidding_amount=i.bid_amount
	


# 	return render(request,"bid_product.html",{'bidding_amount':bidding_amount,'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour})
	


def bid_update(request,id):

	current_user=User.objects.get(username=request.user)
	bid_obj=Bidder_product.objects.filter(bid_by=current_user.id)

	pobj=Product.objects.get(id=id)
	p_img=Product_images.objects.filter(product=id)

	u_obj=User.objects.get(username=pobj.added_by)
	u_name=u_obj.first_name+" "+u_obj.last_name

	close_date=pobj.closing_date.split(":")


	january1st = datetime.datetime(int(close_date[2]),int(close_date[1]),int(close_date[0]))
	
	timesince =  january1st-datetime.datetime.now()
	minutessince = int(timesince.total_seconds() / 60)

	
		
	remaning_hour=int(minutessince/60)

	
	
	close_date="-".join(close_date)

	current_user=User.objects.get(username=request.user)

	b_amount=0

	if request.method == "POST":
		bid_amount=request.POST['bid_amount']

		for i in bid_obj:
			if i.product_id == id :
				bobj=Bidder_product.objects.filter(product_id=id,bid_by=current_user.id)
				bobj.update(bid_amount=bid_amount)
				b_amount=bid_amount
				messages.success(request," You have update bid on this product successfully.")

	return render(request,"bid_product.html",{'pobj':pobj,'p_img':p_img,'cdate':close_date,'uname':u_name,'r_time':remaning_hour,'bidding_amount':b_amount})		

		


def buy_product(request):

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

	return render(request,"buy_product.html",{'pobj':remain_pobj})


def userprofile(request):
	uobj=User.objects.get(username=request.user)
	u_info_obj=UserInfo.objects.get(user_id=uobj.id)


	bobj=Bidder_product.objects.filter(bid_by=uobj.id)

	curent_user_bid_pobj=[]

	d=1

	for i in bobj:
		product_obj=Product.objects.get(id=i.product_id) 
		product_obj.bid_amt=i.bid_amount
		product_obj.s_no=d
		product_obj.bid_id=i.id
		if i.status==0:
			product_obj.status="Waiting"
		elif i.place_status==1:
		 	product_obj.status="Buy Successfully(Cash On Delivery)"
		else:
			product_obj.status="Congratulation you win Click to proceed ."
		curent_user_bid_pobj.append(product_obj)
		d=d+1




	b_obj=Bidder_product.objects.all()

	current_user_sell_product_bid=[]

	k=1

	for i in b_obj:
		pobj=Product.objects.get(id=i.product_id)

		if pobj.added_by_id ==uobj.id:
			
			if pobj in current_user_sell_product_bid:
				pass
			else:
				current_user_sell_product_bid.append(pobj)
				pobj.Sno=k

				k=k+1



	for i in current_user_sell_product_bid:
		product_bid=Bidder_product.objects.filter(product_id=i.id)
		l=1
		for j in product_bid:
			uname=User.objects.get(id=j.bid_by_id)
			j.fullname=uname.first_name+" "+uname.last_name
			umob=UserInfo.objects.get(user_id=j.bid_by_id)
			j.mobile=umob.mobile
			j.sn=l
			l=l+1
			if j.status == 0:
				j.status="Approve"
				i.product_status="Active"
			else:
				j.status = "Sold Successfully"
				i.product_status="Closed"



		i.product_bid=product_bid
		i.num_of_bid=len(product_bid)
					

			
	if request.method=="POST":
		fn=request.POST["first_name"]
		ln=request.POST["last_name"]
		un=request.POST["user_name"]
		pwd=request.POST["password"]
		email=request.POST["email"]
		address=request.POST["address"]
		mob=request.POST["mob"]

		u_obj=User.objects.filter(id=uobj.id)
		u_obj.update(first_name=fn,last_name=ln,username=un,password=make_password(pwd),email=email)

		UserInfo_obj=UserInfo.objects.filter(user_id=uobj.id)
		UserInfo_obj.update(mobile=mob,address=address,user=uobj,password=pwd)

		user=authenticate(username=un,password=pwd)
		login(request,user)

		uobj=User.objects.get(username=request.user)
		u_info_obj=UserInfo.objects.get(user_id=uobj.id)



		messages.success(request," Record updated Successfully.")

		
		
	return render(request,"userprofile.html",{'uobj':uobj,'u_info_obj':u_info_obj,'pobj':curent_user_bid_pobj,'p_obj':current_user_sell_product_bid})


def bid_approve(request,id):
	bobj=Bidder_product.objects.get(id=id)
	bobj_all=Bidder_product.objects.filter(product_id=bobj.product_id)
	for i in bobj_all:
		if id != i.id: #56 ! = 56
			i.delete()
		else:
			bid_status_update=Bidder_product.objects.filter(id=i.id)
			bid_status_update.update(status=1)
			messages.success(request," Congratulation You have sold the item .")
			break;

	return redirect('/bidder/userprofile/')	

def win_proceed(request,id):

	mobj=Pyment_method.objects.all()
	uobj=User.objects.get(username=request.user)
	user_info_obj=UserInfo.objects.get(user_id=uobj.id)
	bobj=Bidder_product.objects.get(id=id)
	pobj=Product.objects.get(id=bobj.product_id)
	bobj.product_name=pobj.name
	bobj.shipping_address=user_info_obj.address



	dobj=datetime.datetime.now()
	date=dobj.strftime("%d")
	month=dobj.month
	year=dobj.year
	rn=random.randint(9999999,1111111111)


	order_id=orderId(date,year,month,rn)
	
	if request.method == "POST":
		p_name=request.POST["p_name"]
		p_price=request.POST["p_price"]
		method=request.POST["pyment_method"]
		address=request.POST["shipping_address"]

		obj=Orders(order_id=order_id,product_name=p_name,total_amt=p_price,address=address,payment_method=method,bid=bobj)
		obj.save()

		b_obj=Bidder_product.objects.filter(id=id)
		b_obj.update(place_status=1)

		messages.success(request," Order placed Successfully .")

		return redirect('/bidder/userprofile/')


	return render(request,"checkout_form.html",{'mobj':mobj,'bobj':bobj})

def orderId(date,year,month,random_number):
	d=str(date)
	m=str(month)
	y=str(year)
	rn=str(random_number)

	return("OD"+"__"+d+m+y+"__"+rn)



def category_delete(request,id):
	cobj=Category.objects.get(id=id)
	cobj.delete()

	messages.success(request," Category delete successfully .")

	return redirect('/categories_list/')


def category_edit(request,id):

	cobj=Category.objects.filter(id=id)

	if request.method=="POST":
		edit_category=request.POST['add_cat']

		cobj.update(catname=edit_category)

		messages.success(request,' Category edit successfully .')

		return redirect('/categories_list/')


	return render(request,'category_edit.html')


def auction_list(request):



	pobj=Product.objects.all()

	s=1

	for i in pobj:
		bobj=Bidder_product.objects.filter(product_id=i.id)

		closing_date=i.closing_date.split(":")


		current_date=datetime.datetime.now()
		old_date = datetime.datetime(int(closing_date[2]), int(closing_date[1]), int(closing_date[0]))


		if len(bobj) == 1:
			
			if(current_date>old_date):
				i.pro_time="Expired"
				i.pro_status="Not Sold"
			else:
				i.pro_time="Not Expired"
				i.pro_status="Not Sold"


			if bobj[0].place_status==1:
				i.pro_status="Sold"	
				if(current_date>old_date):
					i.pro_time="Expired"
					
		else:
			if(current_date>old_date):
					i.pro_time="Expired"
					i.pro_status="Not Sold"
			else:
				i.pro_time="Not Expired"
				i.pro_status="Not Sold"
				





		
		# if len(bobj)==1:
		# 	if bobj[0].place_status==1:
		# 		i.pro_status="Sold"
		# 		if(current_date>old_date):
		# 			i.pro_time="Expired"
		# 			print(i.pro_time)
		# 		else:
		# 			i.pro_time="Not Expired"	
		# 	else:
		# 		i.pro_status="Not Sold"


			

		cobj=Category.objects.get(id=i.cat_id)
		i.cat_name=cobj.catname
		i.des=i.des[:200]+"....."
		i.price=str(i.price)+"/-Rs."
		i.s_no=s
		s=s+1

	return render(request,'auction_list.html',{'pobj':pobj})
	

def admin_delete_product(request,id):

	pobj=Product.objects.filter(id=id)
	pobj.delete()

	messages.success(request,' Product remove successfully .')

	return redirect('/bidder/auction_list/')


def add_new_user(request):

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

		messages.success(request," User created successfully. ")

		return redirect('/bidder/add_new_user/')
		

	return render(request,'add_new_user.html')



def user_list(request):

	uobj=User.objects.filter(is_superuser=0)

	s=1

	for i in uobj:
		i.s_no=s
		s=s+1


	return render(request,'user_list.html',{'uobj':uobj})

def user_delete(request,id):

	uobj=User.objects.get(id=id)
	uobj.delete()

	messages.success(request," User remove successfully . ")

	return redirect('/bidder/user_list/')

def admin_update_detail(request):

	uobj=User.objects.filter(username=request.user)

	u_obj=User.objects.get(username=request.user)

	if request.method=="POST":
		un=request.POST['un']

		up=request.POST['up']

		uobj.update(username=un,password=make_password(up))

		user=authenticate(username=un,password=up)

		login(request,user)

		messages.success(request," Account update successfully .")


	return render(request,'admin_update_detail.html',{'u_obj':u_obj})

def log_out(request):
	logout(request)
	return redirect("/home/")








