from django.db import models

# Create your models here.
class Classes(models.Model):
    classes_name = models.CharField(max_length=200)
    classes_description = models.TextField()
    def __str__(self):
        return self.classes_name
    
class Experts(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='experts/', blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, help_text="Add number with country code, e.g., 919876543210")


    def __str__(self):
        return self.name