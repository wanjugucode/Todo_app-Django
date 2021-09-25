from django.shortcuts import render
from .forms import TaskForm
from.models import Task

# Create your views here.

def register_task(request):
    form=TaskForm()
    return render (request,'register_task.html',{
        'form':form,
    })

def register_task(request):
    if request.method=="POST":
        form=TaskForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TaskForm()
    return render (request,"register_task.html",{ "form":form})

def task_lisk(request):
    tasks=Task.objects.all()
    return render(request,"task_list.html",{"tasks":tasks })
 
def edit_task(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        form=TaskForm(request.POST,request.FILES,instance=task)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TaskForm(instance=task)
    return render(request,'edit_task.html',{'form':form})
    


    
  
 
 



