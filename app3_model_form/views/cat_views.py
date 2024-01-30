from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from app3_model_form.models import Category
from app3_model_form.forms import CategoryForm


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'category/list.html', context)


class CategoryDetailView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        products = category.product_set.all()  # Retrieve associated products
        context = {'category': category, 'products': products}
        return render(request, 'category/detail.html', context)


class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'category/add-edit.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app3:category_list')
        return render(request, 'category/add-edit.html', {'form': form})


class CategoryUpdateView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'category/add-edit.html', {'form': form})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('app3:category_list')
        return render(request, 'category/add-edit.html', {'form': form})


class CategoryDeleteView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        context = {'category': category}
        return render(request, 'category/delete.html', context)

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('app3:category_list')
