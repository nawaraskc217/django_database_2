from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.


def index(request):
    item_list=Item.objects.all()  
    context={
        'item_list':item_list,
    }
    return render(request, 'food/index.html',context)
    

def item(request):
    # item_list=Item.objects.all()
    return HttpResponse("<h1>this is ITEM </h1>")


def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request, 'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request,'food/item-form.html',{'form':form})



# def update_item(request, id):  # Accept id as a parameter
#     item = Item.objects.get(id=id)  # Use id to retrieve the item
#     form = ItemForm(request.POST or None, instance=item)

#     if form.is_valid():
#         form.save()
#         return redirect('index')
    
#     return render(request, 'food/item-form.html', {'form': form, 'item': item})




def update_item(request, id):
    item = get_object_or_404(Item, id=id)  # Fetch item or return 404 if not found
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):  # Accept id as a parameter
    item = Item.objects.get(id=id)  # Use id to retrieve the item


    if request.method=='POST':
        item.delete()

        return redirect('index')
    
    return render(request, 'food/item-delete.html', {'item': item})


