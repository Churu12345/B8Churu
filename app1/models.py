from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(null =True)

# Create your models here.
    class Meta:
        db_table="person"

    def __str__(self):
        return f"{self.name}--{self.address}"