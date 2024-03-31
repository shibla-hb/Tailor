from django.db import models

# customer models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES = ((LIVE, 'live'),(DELETE, 'delete'))
    customer_name = models.CharField(max_length=200)
    address = models.FloatField()
    place = models.FloatField()
    person_name=models.FloatField()
    person_designation=models.FloatField()
    status=models.CharField(max_length=100)
    priority = models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
