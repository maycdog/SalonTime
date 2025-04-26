from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

# Função para adicionar cliente
def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.preco = 0  # inicializa para evitar erro
            cliente.save()  # salva sem os serviços ainda
            form.save_m2m()  # salva os serviços

            # Agora que os serviços foram salvos, calcula o preço total
            cliente.preco = sum(servico.preco for servico in cliente.servicos.all())
            cliente.save()
            return redirect('clientes_listar')
    else:
        form = ClienteForm()
    return render(request, 'agendamentos/adicionar_cliente.html', {'form': form})

# Função para listar clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'agendamentos/exibir_clientes.html', {'clientes': clientes})

# Função para atualizar cliente
def atualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            form.save_m2m()

            cliente.preco = sum(servico.preco for servico in cliente.servicos.all())
            cliente.save()
            return redirect('clientes_listar')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'agendamentos/adicionar_cliente.html', {'form': form})

# Função para deletar cliente
def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('clientes_listar')
