from django.db import models

# customer models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    title=models.CharField(max_length=200)
    product_rate=models.FloatField()
    model_rate=models.FloatField()
    quantity=models.FloatField()
    Amount=models.FloatField()
    image=models.ImageField(upload_to='/media')
    status=models.CharField(max_length=100)
    deliverd_to=models.FloatField()
    delivered_date = models.FloatField()
    priority = models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
