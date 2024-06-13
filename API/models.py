from django.db import models
from django.contrib.auth.models import User 




class Author(models.Model):
    name = models.CharField(max_length=255)

class Star(models.Model):
    number = models.IntegerField(default=0)
    

    @property
    def avarage(self):
        return self.number // len(self.customuser_set.all())



class Book(models.Model):
    star = models.OneToOneField("Star", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.PROTECT)
    is_available = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title 








class CustomUser(models.Model):
    star = models.ManyToManyField(Star)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)




    
class Comment(models.Model):
    content = models.TextField(max_length=1023)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    
    

