from django.db import models
# Create your models here.


class Subscribe(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class users(models.Model):
    email = models.EmailField()
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=20)

class myblog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=300, default='')
    blog_desc = models.TextField(default='')
    time_req = models.IntegerField(null=True)
    image = models.ImageField(upload_to='app1/images',default='')
    code = models.TextField(max_length=1000, null=False, blank=True,default='')
    youtube_link = models.CharField(max_length=300, null=False, blank=True,default='')
    pub_date = models.DateField()
    featured = models.BooleanField(default=False)


class Contact(models.Model):
    personname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length =1000)


class Gallery(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='app1/gallery')
    date = models.DateTimeField()
    featured = models.BooleanField()