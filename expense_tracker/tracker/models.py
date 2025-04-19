from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model
class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)

#expense category
class Category(models.Model):
    user = models.ForeignKey(CustomUser,on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
# expense Model
class Expense(models.Model):
    user = models.ForeignKey(CustomUser,on_delete= models.CASCADE)
    category = models.ForeignKey(Category,on_delete= models.SET_NULL,null= True)
    title = models.CharField(max_length= 100)
    amount = models.DecimalField(max_digits= 10, decimal_places= 2)
    notes = models.TextField(blank= True)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.amount}"


