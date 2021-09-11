from django.shortcuts import render,redirect

from . models import Category

from django.contrib.auth.models import User

from django.contrib import messages


from . models import Product,Product_images

from . models import City,Feedback

from bidder.models import Bidder_product

# Create your views here.

def sellproduct(request):
	all_cat_obj=Category.objects.all()
	all_city=City.objects.all()

	if request.method=="POST":
		pro_images=request.FILES.getlist("p_imgs")
		name=request.POST["p_name"]
		price=request.POST["p_price"]
		# qty=request.POST["p_qty"]
		cat_id=request.POST["cat_id"]
		closing_date=request.POST["p_date"]
		cover_img=request.FILES["p_img"]
		des=request.POST["p_des"]
		city=request.POST["p_city"]

		uobj=User.objects.get(username=request.user)

		cobj=Category.objects.get(id=cat_id)

		date=closing_date.split("-")
		date1=[]
		for i in range(1,len(date)+1):
			date1.append(date[-i])


		ndate=":".join(date1)

		pobj=Product(name=name,price=price,des=des,closing_date=ndate,cat=cobj,cover_img=cover_img,added_by=uobj,city=city)
		pobj.save()

		for i in pro_images:
			Product_images_obj=Product_images(product=pobj,product_images=i)
			Product_images_obj.save()


		messages.success(request," Record Added Successfully...")

	return render(request,"sellproduct.html",{'cobj':all_cat_obj,'city_obj':all_city})





def search(request):

	cobj=Category.objects.all()

	bobj=Bidder_product.objects.filter(status =1)

	b_obj=[]

	search_product=[]

	for i in bobj:

		p_obj=Product.objects.get(id=i.product_id)

		b_obj.append(p_obj)


	
	

	if request.method=="POST":
		pn=request.POST["p_name"]
		cat_id=request.POST['cat_id']

		pobj=Product.objects.filter(cat_id=cat_id)



		

		for i in pobj:
			if i not  in b_obj:


				if pn in i.name or pn in i.des:



					search_product.append(i)


					
			
		

	return render(request,'search.html',{'cobj':cobj,'pobj':search_product})


def contact_us(request):

	if request.method == "POST":
		un=request.POST["name"]
		ue=request.POST["email"]
		um=request.POST["mob"]
		uc=request.POST["comment"]

		uobj=User.objects.get(username=request.user)

		fobj=Feedback(name=un,email=ue,mobile=um,comment=uc,send_by=uobj)
		fobj.save()

		messages.success(request," Feedback  send successfully .")

	return render(request,'contact_us.html')
