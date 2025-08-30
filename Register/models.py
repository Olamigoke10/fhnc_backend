from django.db import models



# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=100, blank=True) 
    
    def __str__(self):
        return self.title
    

class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="registrations")
    message = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} -  {self.course.title}"
    
    