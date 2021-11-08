from django.shortcuts import render
import json
from django.http import HttpResponseRedirect
from decouple import config
from django.contrib.auth import logout as django_logout
from urllib.parse import urlencode
# Create your views here.

def index(request):
    return render(request,"index.html")
    

def profile(request):
    user = request.user

    auth0_user = user.social_auth.get(provider='auth0')

    #print(dir(auth0_user))

    user_data = {
        'user_id' : auth0_user.uid,
        'name' : auth0_user.name,
        'picture' : auth0_user.extra_data['picture']
    }

    context = {
        'user_data' : json.dumps(user_data,indent=4),
        'auth0_user' : auth0_user
    }

    return render(request,"profile.html",context)


def logout(request):
    django_logout(request)

    domain = config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})

    logout_redirect_url = f'http://{domain}/v2/logout?client_id={client_id}&returnTo{return_to}'

    return HttpResponseRedirect(logout_redirect_url)
