from django.contrib import admin
from .models import Sura,Oyat

class SuraAdmin(admin.ModelAdmin):
    list_display = ("id","name",)
    # prepopulated_fields = {"slug": ("name",)}

class OyatAdmin(admin.ModelAdmin):
    list_display = ("id","sura","arabic_text","uzbek_text",)

admin.site.register(Sura,SuraAdmin)
admin.site.register(Oyat,OyatAdmin)