from __future__ import unicode_literals
from .models import User,Friend,Other
from django.shortcuts import render, redirect
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    return render(request, 'beltapp/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
        user = User.objects.get(id=request.session['user_id']),
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'friends':Friend.objects.all(),
        'others' :Other.objects.all(),
    }
    return render(request, 'beltapp/success.html', context)

def friendprofile(request, friend_id):
    profile = Friend.objects.get(id=friend_id)
    context = {
        'friend' : profile
    }
    return render(request, 'beltapp/show.html', context)

def othersprofile(request, other_id):
    profile = Other.objects.get(id=other_id)
    context = {
        'other' : profile
    }
    return render(request, 'beltapp/notfiend.html', context)


# def addfriend(request, other_id):
#     # User.userManager.addFriend(request.session['id'], id)
#     return redirect('/success')
    
def addfriend(request, other_id):
    this_other = Other.objects.get(id=other_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_other.other.add(this_other)
    #  new_friend = User.objects.get(id=request.session['user_id']).other.add(Other.objects.get(id=other_id))
    

    return redirect('/success')

def removefriend(request, friend_id):
    Friend.objects.get(id=friend_id).delete()
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')