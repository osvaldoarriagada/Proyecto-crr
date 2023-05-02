from django.contrib import messages
from django.shortcuts import render
from import_export import resources
from import_export.formats import base_formats
from .resources import TipoResource
from django.http import HttpResponse
from tablib import Dataset

def exportar_datos(request):
    resource = TipoResource()
    dataset = resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos.csv"'
    return response

def importar_datos(request):
    if request.method == 'POST':
        resource = TipoResource()
        dataset = Dataset()
        nuevos_datos = request.FILES['archivo']
        imported_data = dataset.load(nuevos_datos.read().decode('utf-8'), format='csv')
        result = resource.import_data(dataset, dry_run=True)  # Para validar los datos sin guardarlos
        if not result.has_errors():
            resource.import_data(dataset, dry_run=False)  # Para guardar los datos
            messages.success(request, 'Los datos se importaron correctamente.')
        else:
            messages.error(request, 'Ocurrió un error al importar los datos.')
    return render(request, 'importar.html')