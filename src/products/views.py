# from django.views import ListView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.


# products list view using class
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context


# products list view using functions
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


# products Detail view using class
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        return context


# products detail view using functions
def product_detail_view(request, pk=None, *args, **kwargs):
    print(args)
    print(kwargs)
    # instance = Product.objects.get(pk=pk)  # pk can be replaced by id
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
