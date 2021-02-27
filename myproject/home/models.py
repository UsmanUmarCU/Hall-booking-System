from django.db import models

# Create your models here.
class Hall(models.Model):
    Hall_id = models.AutoField
    Hall_name = models.CharField(max_length=50)
    Hall_capacity = models.IntegerField()
    Hall_area = models.TextField()
    Hall_price = models.IntegerField()
    Hall_catering = models.BooleanField()
    Hall_image = models.ImageField(upload_to="home/image",default="")


    def __str__(self):
        return self.Hall_name
