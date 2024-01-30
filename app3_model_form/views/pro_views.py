from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from app3_model_form.models import Product
from app3_model_form.forms import ProductForm


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        category = product.category  # Retrieve associated category
        context = {'product': product, 'category': category}
        return render(request, 'product/detail.html', context)


class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product/add-edit.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app3:product_list')
        return render(request, 'product/add-edit.html', {'form': form})


class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product/add-edit.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('app3:product_list')
        return render(request, 'product/add-edit.html', {'form': form})


class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'product/delete.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('app3:product_list')
