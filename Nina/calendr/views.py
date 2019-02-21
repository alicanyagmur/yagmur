from django.shortcuts import render,HttpResponseRedirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages

# Create your views here.

def Calendar_View(request):
    return render(request,'calendar/calendar.html')


def Reservation_View(request):
    if request.user.is_authenticated():

        form = ReservationForm(request.POST or None)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Başarılı bir şekilde oluşturdunuz.') # Trans edilecek
            return HttpResponseRedirect(reservation.get_absolute_url())

        context = {
            'form': form,
        }
        return render(request, 'calendar/calendar.html', context)

    else:
        return render(request, 'account/login.html')