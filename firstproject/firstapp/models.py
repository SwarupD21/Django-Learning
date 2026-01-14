from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model):
    TYPE_CHOICE=[
        ('ML','MASALA'),
        ('EL','ELACHI'),
        ('PL','PLAIN')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added=models.DateField(default=timezone.now)
    type = models.CharField(max_length=100,choices=TYPE_CHOICE,default='ML')
    description = models.TextField(max_length=500,default='')

    def __str__(self):
        return self.name

# ONE TO MANY
class review(models.Model):
    chai = models.ForeignKey(Content,on_delete=models.CASCADE,related_name='chai')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    
# MANY TO MANY
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varity = models.ManyToManyField(Content,related_name='stores')

    def __str__(self):
        return self.name
    
# ONE TO ONE
class Certificate(models.Model):
    chai = models.OneToOneField(Content,on_delete=models.CASCADE,related_name='certificate') 
    certificate = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'