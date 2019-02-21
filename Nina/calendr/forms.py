from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=[
            'language_selection',
            'reservation_date',
            'start_time',
            'end_time',
        ]