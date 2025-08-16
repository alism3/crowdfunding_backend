from django.db import models

# Create your models here.
class Fundraiser(models.Model): #We inherit our class from the built-in models.Model that comes with Django
    title = models.CharField(max_length=200) # the title field cannot be more than 200 characters long
    description = models.TextField() 
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) #date_created field should be automatically set with the current date when a new record is created.

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser' ,
        related_name='pledges',
        on_delete=models.CASCADE
    )
##In plain English, we have basically told Django this...

#"Hey, make me a table in the database called Fundraiser, and give it the following columns:

#title - this field should contain short strings of characters
#description - this field should contain longer blocks of text
#goal - this field should contain an integer
#etc... (EVERYTIME I CREATE A NEW MODEL I HAVE TO MIGRATE)