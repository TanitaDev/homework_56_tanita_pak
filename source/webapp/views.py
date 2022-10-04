from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product


def index_view(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.order_by('category', 'name').filter(name__icontains=search_query).exclude(remainder='0')
        context = {
            'products': products
        }
        return render(request, 'index.html', context)
    else:
        products = Product.objects.order_by("category", "name")
        context = {
            'products': products
        }
        return render(request, 'index.html', context)

def single_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)
