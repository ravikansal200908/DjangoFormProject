from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from app3_model_form.models import Order
from app3_model_form.forms import OrderForm


class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'order/list.html', {'orders': orders})


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        products = order.products.all()  # Retrieve associated products
        context = {'order': order, 'products': products}
        return render(request, 'order/detail.html', context)


class OrderCreateView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'order/add-edit.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app3:order_list')
        return render(request, 'order/add-edit.html', {'form': form})


class OrderUpdateView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(instance=order)
        return render(request, 'order/add-edit.html', {'form': form})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('app3:order_list')
        return render(request, 'order/add-edit.html', {'form': form})


class OrderDeleteView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'order/delete.html', {'order': order})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect('app3:order_list')
