from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from estacionamento.forms import LocacaoForm
from estacionamento.models import Locacao


def list_locacao(request):
    estacionamentos = Locacao.objects.all()
    print("1")
    return render(request, 'estacionamento.html', {'estacionamentos': estacionamentos})


def create_locacao(request):
    form = LocacaoForm(request.POST or None)
    print("2")
    if form.is_valid():
        print("3")
        form.save()
        return redirect('list_locacao')

    return render(request, 'estacionamento-form.html', {'form': form})


def update_locacao(request, id):
    locacao = Locacao.objects.get(id=id)
    form = LocacaoForm(request.POST or None, instance=locacao)

    if form.is_valid():
        form.save()
        return redirect('list_locacao')

    return render(request, 'estacionamento-form.html', {'form': form, 'locacao': locacao})


def delete_locacao(request, id):
    locacao = Locacao.objects.get(id=id)

    if request.method == 'POST':
        locacao.delete()
        return redirect('list_locacao')

    return render(request, 'estacionamento-delete-confirm.html', {'locacao': locacao})

