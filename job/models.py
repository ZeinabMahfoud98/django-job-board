from django.db import models

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
    title=models.CharField(max_length=100)

    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='rel_category')

    def __str__(self) -> str:
        return self.title
