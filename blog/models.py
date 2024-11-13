from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    biography = models.CharField(max_length=301,blank=True,null=True)
    city = models.CharField(max_length=120,blank=True,null=False)
    foto=models.ImageField(null=True,blank=True,upload_to='profil_fotolari/%Y/%m')
    birthday = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.user.username
    

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height>600 or img.width>600:
                output_size=(600,600)
                img.thumbnail(output_size)
                img.save(self.foto.path)
    class Meta:
        verbose_name_plural='User Profiles'
    

class Categories(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural='Categories'


class Post(models.Model):
    post_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Categories,blank=True)
    STATUS_CHOICES = [
        (True,'Published'),
        (False,'Draft'),
    ]
    status = models.BooleanField(choices=STATUS_CHOICES,default=True)

    def __str__(self):
        return f"{self.title} - {str(self.created_at)}"
    
    class Meta:
        verbose_name_plural='Posts'

class Comment(models.Model):
    comment_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment_user} - {self.post}"

    class Meta:
        verbose_name_plural='Comments'

