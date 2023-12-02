from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Pin_code = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")