from django.db import models

# Create your models here.

class Objective(models.Model):
	objective=models.CharField(max_length=1000)
	mission=models.CharField(max_length=1000)
	vision=models.CharField(max_length=1000)

	def __str__(self):
		return self.objective+' - '+self.mission