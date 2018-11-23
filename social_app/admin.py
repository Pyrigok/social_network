from django.contrib import admin
from .models import Message_Model


class Message_Admin(admin.ModelAdmin):
	list_display = ['author', 'whom', 'status', 'created_on']
	ordering = ['author', 'whom', 'status', 'created_on']

admin.site.register (Message_Model, Message_Admin)