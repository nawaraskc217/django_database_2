from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name
 
    img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpf1eoNbsWblTDxgrmnzqLSutOOZBoo69CNg&s'
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image=models.CharField(max_length=500,default=img)


    

