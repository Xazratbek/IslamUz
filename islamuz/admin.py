from django.contrib import admin
from .models import Iymon, Zakot, Namoz, Ruza, Haj

class IymonAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}

class ZakotAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}

class NamozAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}

class RuzaAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}

class HajAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Iymon, IymonAdmin)
admin.site.register(Zakot, ZakotAdmin)
admin.site.register(Namoz, NamozAdmin)
admin.site.register(Ruza, RuzaAdmin)
admin.site.register(Haj, HajAdmin)
