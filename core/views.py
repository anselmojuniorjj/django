from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .form import ClienteForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    return render(request, 'core/base.html')

def listagem(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/listagem.html', {'clientes' : clientes})

@login_required
def incluir(request):
    # data ={}
    form = ClienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(listagem)

    # data['form'] = form
    return render(request, 'core/incluir.html', {'form' : form})

@login_required
def alterar(request, pk):
    data = {}
    # cliente = Cliente.objects.get(pk=pk)
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect(listagem)

    data['form'] = form
    data['cliente'] = cliente
    return render(request, 'core/incluir.html', data)

@login_required
def excluir(request, pk):
        # cliente = Cliente.objects.get(pk=pk)
        cliente = get_object_or_404(Cliente, pk=pk)
        if request.method == 'POST':
            cliente.delete()
            return redirect('url_listagem')
            
        return render(request, 'core/confirma.html', {'cliente' : cliente})

# def login(request):
#     return render(request, 'core/login.html')
    