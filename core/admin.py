from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    fields = ['nome', 'sobrenome', 'idade', 'foto']
    list_display = ['nome', 'sobrenome', 'idade', 'email', 'foto', 'dat_nasc']

admin.site.register(Cliente, ClientAdmin)