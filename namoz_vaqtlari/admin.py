from django.contrib import admin
from .models import NamozVaqtlari

class NamozVaqtlariAdmin(admin.ModelAdmin):
    list_display = ("mintaqa", "bomdod","quyosh","peshin","asr","shom","xufton")
    prepopulated_fields = {"slug": ("mintaqa",)}

admin.site.register(NamozVaqtlari,NamozVaqtlariAdmin)