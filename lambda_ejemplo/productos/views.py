from django.shortcuts import render
from .models import Producto

def productos_view(request):
    productos = Producto.objects.all()

    # Ordenar usando expresión lambda
    productos_ordenados = sorted(productos, key=lambda p: p.precio)

    return render(request, 'productos.html', {
        'productos': productos_ordenados
    })