from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

@login_required
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'username': request.user.username,
    })
