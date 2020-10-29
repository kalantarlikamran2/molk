from django.contrib import admin
from list.models import Telebe

class TelebeAdmin(admin.ModelAdmin):
    list_display = ['adi','soyad','ata','fakulte' ,'grup']
    list_display_links = ['adi','soyad','grup']
    class Meta:
        model = Telebe
admin.site.register(Telebe,TelebeAdmin)
# Register your models here.
