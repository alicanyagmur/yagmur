from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def Home_View(request):
    if request.user.is_authenticated():
        user_full_name = (request.user.first_name+ ' ' + request.user.last_name)
        user_date_joined = request.user.date_joined
        context = {
            'user_full_name': user_full_name,
            'user_date_joined': user_date_joined
        }
        return render(request,'home.html',context)

    else:
        return render(request,'account/login.html')