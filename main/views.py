from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Chat
from django.core import serializers

# Create your views here.
def index(request):
    if( 'name' in request.session):
        all_users = User.objects.raw('SELECT * FROM main_user');
        communities = User.objects.raw('SELECT community FROM main_user');
        return render(request, 'main/dashboard.html',{'page':'dash', 'all_users':all_users, 'communities':communities,'active_user':request.session['name']});
    return render(request, 'main/index.html',{'page':'home'});
def login(request):
    user_instance = User(name = request.POST['name'], community = "random");
    user_instance.save();
    request.session['name'] = request.POST['name']
    return HttpResponseRedirect("/")

def logout(request):
    if( 'name' in request.session):
        del request.session['name']
    return HttpResponseRedirect("/")
def new_msg(request):
    sender = request.POST['name']
    msg = request.POST['message']
    chat_instance = Chat(name = sender, message = msg, new = "yes")
    chat_instance.save();
    return HttpResponse('ok');
def add_chat(request):
    try:
      chat = Chat.objects.raw('SELECT * FROM main_chat WHERE new = "yes"')
      SomeModel_json = serializers.serialize("json", chat)
      for x in chat:
          print x.name
          print x.message
          print x.new
          print x.pk
          if request.session['name'] != x.name:
              Chat.objects.filter(name = x.name, message= x.message, pk = x.pk).update(new = "no")
      return HttpResponse(SomeModel_json);
    except Chat.DoesNotExist:
      # we have no object!  do something
      return HttpResponse("none");
def all_msg(request):
    try:
      chat = Chat.objects.raw('SELECT * FROM main_chat WHERE new = "no"')
      SomeModel_json = serializers.serialize("json", chat)
      return HttpResponse(SomeModel_json);
    except Chat.DoesNotExist:
      # we have no object!  do something
      return HttpResponse("none");
