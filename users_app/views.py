from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate

import json
import hashlib

from .models import UserForm


def home(request):
    try:
        body = request.POST
        user = authenticate(username=body.get('username'),
                            password=body.get('password'))

        # Auth failed
        if user is None:
            return render(request, "login.html", {'username': body.get('username')})

        # Login success
        return render(request, "home.html")
    except:
        return HttpResponseBadRequest("Bad Request")


def login(request):
    return render(request, "login.html")


def get_user(request, username):
    try:
        user = UserForm.objects.filter(username=username).values()[0]
        return JsonResponse({"response": {
            "message": "success",
            "user": json.dumps(user)
        }})
    except Exception as e:
        print(e)
        return JsonResponse({"response": {
            "message": "fail"}})


def save_user(request):
    try:
        req_body = json.loads(request.body)
        hashed_pw = hashlib.sha256(
            req_body.get('password').encode()).hexdigest()

        req_body['password'] = hashed_pw
        try:
            user_form = UserForm.objects.create(**req_body)
        except IntegrityError as e:
            print("INTEGRITY ERROR")
            return JsonResponse({"message": "Error - username or email already exists"})

        return JsonResponse({"message": "success"})
    except Exception as e:
        return JsonResponse({"message": "error"})
