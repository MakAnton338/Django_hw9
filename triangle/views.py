from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def triangle(request):
    form = HypotenuseForm(request.GET or None)
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = round((a**2 + b**2)**0.5)
        context = {'a': a, 'b': b, 'c': c, 'form': form}
    else:
        context = {'form': form}
    return render(request, 'hypotenuse.html', context)


def person_list(request):
    users = PersonModels.objects.all()
    return render(request, 'user_list.html', {'users': users})


def person_register(request):
    if request.method == 'POST':
        user_form = PersonForm(request.POST)

        if user_form.is_valid():
            obj = user_form.save()
            return redirect('triangle:person_upd', pk=obj.pk) #example: redirect

    else:
        user_form = PersonForm()

    return render(request, 'user_registration.html', {'form': user_form})


def person_upd(request, pk):
    obj = get_object_or_404(PersonModels, pk=pk)

    if request.method == 'POST':
        user_form = PersonForm(request.POST, instance=obj)

        if user_form.is_valid():
            obj = user_form.save()
            return redirect('triangle:person_register')

    else:
        user_form = PersonForm(instance=obj)

    return render(request, 'user_upd.html', {'form': user_form, 'obj': obj})