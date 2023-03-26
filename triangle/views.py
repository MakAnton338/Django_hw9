from django.shortcuts import render
from .forms import HypotenuseForm


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