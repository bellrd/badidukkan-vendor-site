from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from firebase_admin import auth
from api import firebase

from api.models import User


def login_handler(request):
    if request.method == 'GET':
        if not request.user.is_anonymous:
            return HttpResponseRedirect(redirect_to="/admin")

        return render(request, 'api/login.html')

    id_token = request.POST.get('idToken', None)
    decoded_token = auth.verify_id_token(id_token)
    verified_user = auth.get_user(decoded_token['uid'])
    mobile_number = verified_user.phone_number[-10:]
    user, created = User.objects.get_or_create(mobile_number=mobile_number,
                                               defaults={"password": "somepassword", "is_staff": True,
                                                         "is_vendor": True})
    login(request, user)
    return HttpResponseRedirect(redirect_to="/admin")


def logout_handler(request):
    return render(request, "api/logout.html")