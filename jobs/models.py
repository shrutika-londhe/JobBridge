from django.db import models

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')  # Make sure media settings are correct
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.position}"
