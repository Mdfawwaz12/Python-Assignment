from django.shortcuts import render, redirect, get_object_or_404
from .forms import VisitorForm
from .models import Visitor

def add_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_visitor')
            # return redirect('visitor_list') 
    else:
        form = VisitorForm()

    return render(request, 'visitors/add_visitor.html', {'form': form})

def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})

def update_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, pk=visitor_id)

    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm(instance=visitor)

    return render(request, 'visitors/update_visitor.html', {'form': form, 'visitor': visitor})

def delete_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, pk=visitor_id)

    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor_list')

    return render(request, 'visitors/delete_visitor.html', {'visitor': visitor})
