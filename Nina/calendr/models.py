from django.db import models

# Create your models here.


class Reservation(models.Model):
    user = models.ForeignKey('auth.User',related_name='User_Reservation')
    language_selection = models.DateField(max_length=20)
    reservation_date = models.DateField(max_length=50)
    start_time = models.TimeField(max_length=20)
    end_time = models.TimeField(max_length=20)
