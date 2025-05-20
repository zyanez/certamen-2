from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from .models import Reminder
from .forms import ReminderForm
import json

def index(request):
    reminders = Reminder.objects.all().order_by("-important")
    return render(request, "index.html", {"reminders": reminders})

@csrf_protect
def add_reminder(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = ReminderForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return HttpResponseBadRequest()
    
@csrf_protect
def update_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id)
    if request.method == "PATCH":
        data = json.loads(request.body)
        form = ReminderForm(data, instance=reminder)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        return HttpResponseBadRequest()
    
@csrf_protect
def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id)
    if request.method == "DELETE":
        reminder.delete()
        return HttpResponse(status=200)
    