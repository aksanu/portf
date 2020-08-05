from django.shortcuts import render,redirect
from .models import portfolioImages , subImages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def home(request):
	image= portfolioImages.objects.all()
	return render(request, 'portfolio/index.html',{'image':image})

def upload(request):
	
	if request.method == 'POST':
		title = request.POST.get('title')
		desc = request.POST.get('desc')

		# p_photo= request.POST.get('Profile')
		p_photo=request.FILES['Profile']

		fs = FileSystemStorage()
		filename = fs.save(p_photo.name, p_photo)
		uploaded_file_url = fs.url(filename)
		
		user_data= portfolioImages(images=p_photo , title=title, description=desc)
		user_data.save()
		return redirect('index')

	return render(request, 'portfolio/create.html')


def details(request, id):
	obj=portfolioImages.objects.get(id=id)
	new=obj.subimages_set.all()

	return render(request, 'portfolio/details.html', {'obj':obj, 'new':new})

def more_upload(request, id):
	if request.method== 'POST':
		obj=portfolioImages.objects.get(id=id)
		p_photo=request.FILES['Profile']
		fs = FileSystemStorage()
		filename = fs.save(p_photo.name, p_photo)
		uploaded_file_url = fs.url(filename)
		print(uploaded_file_url)
		print(filename)
		more_img= subImages(img=p_photo, portfolio=obj)
		more_img.save()
		
		return redirect('index')
	return render(request, 'portfolio/more_image.html')



def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pass1']
		user = auth.authenticate(username=username, password=password)

		if (user is not None) and (password == password):
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'invalid credentials')
			return redirect('login')
	else:
		return render(request, 'account/login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')

def contact(request):
	pass