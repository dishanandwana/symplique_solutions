from django.contrib import admin
from django.urls import path

from reminder.views import ReminderList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reminders/', ReminderList.as_view(), name='reminder-list'),
]
