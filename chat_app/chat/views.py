from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
from django.core import serializers

# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    print(room)

    context = {
        'username':username,
        'room_name': room,
        'room_details' : room_details
    }


    return render(request, 'room.html', context)


def checkRoom(request):
    room = request.POST['room']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        pass
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
    
    return redirect('/'+room+'/?username='+username)

def send(request):
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']

    new_message = Message.objects.create(
        user = username,
        room = room_id,
        value = message,
    )

    new_message.save()

    return HttpResponse('Message Sent Successfully')


def getMessages(request,room):
    room_details = Room.objects.get(name = room)

    messages = Message.objects.filter(room = room_details.id)
    
    # What I need Value, date, user, room
    # for msg in 
    

    # serialize queryset
    serialized_queryset = serializers.serialize('json', messages)
    

    return JsonResponse({
        'messages': serialized_queryset
    })