from django.contrib import admin
from .models import Especialidad,Tipo, Conmorbilidad, Ingreso

# Register your models here.
admin.site.register(Especialidad)
admin.site.register(Tipo)
admin.site.register(Conmorbilidad)
admin.site.register(Ingreso)
