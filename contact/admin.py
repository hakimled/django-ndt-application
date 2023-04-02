from django.contrib import admin
from .models import Message

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first','last','message')



admin.site.register(Message , ContactAdmin)
