from django.contrib import admin

# Register your models here.
from .models import *
class UstozAdmin(admin.ModelAdmin):
    list_display = [""]


admin.site.register(Notebook)
admin.site.register(Universiter)
admin.site.register(Talaba)
admin.site.register(Foydalanuvchi)
admin.site.register(Aktyor)
admin.site.register(Rejissor)
admin.site.register(Kino)
admin.site.register(Profil)
admin.site.register(Kurs)
admin.site.register(Xarid)
admin.site.register(Izoh)
admin.site.register(Tanlangan)
admin.site.register(Imtixon)
admin.site.register(Nazoratchi)
admin.site.register(Natija)
admin.site.register(Ustoz)
admin.site.register(Fan)
