from django.shortcuts import render, redirect
from .models import Todolist
from .form import EditForm
from django.contrib import messages


def home(request):
    items = Todolist.objects.all()
    context = {'items':items,}
    return render(request,'home.html',context)

def additem(request):
    form = EditForm()
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Item Added successfully')
            return redirect('home')

    context = {'form': form}
    return render(request,'edit.html',context)


def delete(request,pk):
    item = Todolist.objects.get(id=pk)
    item.delete()
    return redirect ('home')

def edit(request,pk):
    item = Todolist.objects.get(id=pk)
    form = EditForm(instance=item)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'item':item, 'form': form}
    return render(request,'edit.html',context)

def crossoff(request,pk):
    item = Todolist.objects.get(id=pk)
    item.complete = False
    item.save()
    return redirect('home')

def uncrossoff(request,pk):
    item = Todolist.objects.get(id=pk)
    item.complete = True
    item.save()
    return redirect('home')

    