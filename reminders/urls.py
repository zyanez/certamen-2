from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/reminders/", views.add_reminder, name="add_reminder"),
    path("api/reminders/<uuid:reminder_id>/", views.update_reminder, name="update_reminder"),
    path("api/reminders/<uuid:reminder_id>/delete/", views.delete_reminder, name="delete_reminder")
]