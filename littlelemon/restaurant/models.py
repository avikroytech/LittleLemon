from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
	name = models.CharField(max_length=255)
	no_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
	bookingdate = models.DateTimeField()

	def __str__(self):
		return f"{self.name} - Guests: {self.no_of_guests}"

class MenuItem(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	inventory = models.IntegerField(validators=[MaxValueValidator(5)])

	def __str__(self):
		return f"{self.title}"
