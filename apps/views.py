from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DeleteView

from apps.models import Product


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect("product_list")


def update_product(request):
    if request.method=='POST':
        print('nimadir')
        if Product.objects.filter(name=request.POST['old_name']):
            print('kimdir')
            Product.objects.update(
                name=request.POST['title'],
                price=request.POST['price'],
            )
    return redirect('product_list')


def update_page(request):
    return render(request, 'update_product.html')
