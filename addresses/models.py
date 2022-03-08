from django.db import models

# Create your models here.


# 어떤 컬럼을 갖고있는지 정하면 됨.
class Addresses(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']



