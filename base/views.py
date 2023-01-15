from django.shortcuts import render,get_object_or_404
from .models import Item,OrderItem,Order
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.views.generic import ListView,DetailView,View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class OrderSummery(LoginRequiredMixin,View):
    def get(self,*args,**kwrgs):
        try : 
            order = Order.objects.get(user=self.request.user,ordered=False)
            context = {
                'object' : order
            }
            return render(self.request,'order_summary.html',context)
        except ObjectDoesNotExist : 
            messages.error(self.request , 'you dont have an active order')
            return redirect('/')

       


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'

class HomeView(ListView):
    model = Item
    paginate_by = 8
    template_name = 'home.html'

def home(request):
    items = Item.objects.all()
    context ={
        'items' : items
    }

    return render (request,'home.html',context)

def checkout(request):
    items = Item.objects.all()
    context ={
        'items' : items
    }

    return render (request,'checkout.html',context)

def product(request):
    return render (request,'product.html')


@login_required
# add to cart
def add_to_cart(request,slug):
    item = get_object_or_404(Item,slug=slug)
    order_item ,created= OrderItem.objects.get_or_create(
        item=item,
        user = request.user,
        ordered = False

    )
    order_qs = Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request,'this quantity was updated')
        else : 
            messages.info(request,'this item was added to your cart')
            order.items.add(order_item)
    else :
        orderedDate = timezone.now()
        order = Order.objects.create(user=request.user,orderedDate=orderedDate)
        order.item.add(order_item)
        messages.info(request,'this item was added to your cart')
    return redirect('base:product',slug=slug)



@login_required
def remove_from_cart(request,slug):
    item = get_object_or_404(Item,slug=slug)
    order_qs = Order.objects.filter(
        user=request.user
        ,ordered=False
        )

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item = item ,
                user = request.user , 
                ordered = False
            )[0]
            order.items.remove(order_item)  
            messages.info(request,'this item was removed from your cart')
        else : 
            messages.info(request,'this item was not in your cart')
            return redirect('base:product',slug=slug)
    else :
        # add a message saying the user doesnt have an order
        messages.info(request,'you dont have an active order')
        return redirect('base:product',slug=slug)


    return redirect('base:product',slug=slug)


