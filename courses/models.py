from django.db import models

class Enrollment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=30, blank=True, null=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.CharField(max_length=10, blank=True, null=True)
    cvv = models.CharField(max_length=10, blank=True, null=True)
    paypal_email = models.EmailField(blank=True, null=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.course}"
