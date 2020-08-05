from django.db import models
import random
from string import ascii_uppercase
from PIL import Image 
# from django.utils.six import StringIO
# from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.
a=ascii_uppercase
newword= ''
newword=random.choice(a)

class portfolioImages(models.Model):
	title = models.CharField(max_length=500 , null= True , blank=True, default=newword)
	images = models.ImageField(upload_to='images/' , default='blank.jpg')
	description = models.TextField(null= True , blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		ordering = ['-pub_date']

class subImages(models.Model):
	img= models.ImageField(upload_to='images/' , default='blank.jpg')
	portfolio = models.ForeignKey(portfolioImages, on_delete=models.CASCADE, null= True , blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.img.path)
		output_size = (900, 500)
		img.thumbnail(output_size)
		img.save(self.img.path)



