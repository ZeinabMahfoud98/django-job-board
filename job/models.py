from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Job(models.Model):
    FULL_TIME="full time"
    PART_TIME="part time"
    JOB_TYPE=[
        (FULL_TIME,"Full Time Work"),## first for DB second for human
        (PART_TIME,"Part Time Work")
    ]
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='rel_category')
    image=models.ImageField(upload_to='jobs/',blank=True,null=True)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        ##logic for slug
        self.slug=slugify(self.title)
        ##logic for base save
        super(Job,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.title
    

class Apply(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    website=models.URLField()
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField()
    created=models.DateTimeField(auto_now=True)
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
