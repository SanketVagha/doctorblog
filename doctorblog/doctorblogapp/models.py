from django.db import models

# Create your models here.

class Categories(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 122)
    status = models.IntegerField(default = 1)

    def __str__(self):
        return self.id
    
class User(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    password = models.CharField(max_length = 122)
    status = models.IntegerField(default = 1)

    def __str__(self):
        return self.id
    
class Blog(models.Model):
    id = models.AutoField(primary_key= True)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    categoryId = models.ForeignKey(Categories , on_delete = models.CASCADE)
    title = models.CharField(max_length = 1000)
    blog_image = models.ImageField(upload_to= "upload/", max_length= 1000, blank= True, default= None)
    summary = models.CharField(max_length = 1000)
    content = models.CharField(max_length = 1000)
    status = models.IntegerField(default = 1)

    def __str__(self):
        return self.id
    

