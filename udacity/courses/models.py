from django.db import models
from django.urls import reverse
# Create your models here.
class DummyDetail(models.Model):
	Gender_choise=(('male','Male'),('female','Female'))
	name=models.CharField(max_length=200)
	gender=models.CharField(max_length=50, choices=Gender_choise)
	mobile=models.CharField(max_length=50)
	email=models.CharField(max_length=200)

	def __str__(self):
		return self.name+'   -    '+self.mobile

	def get_absolute_url(self):
		return reverse('dummy-detail',kwargs={'pk':self.pk})