from django import forms
from .models import Cliente, Servico

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'servicos', 'telefone', 'email', 'horario']
        widgets = {
            'horario': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona o widget de múltiplos serviços ao campo servicos
        self.fields['servicos'].widget = forms.CheckboxSelectMultiple()
        self.fields['servicos'].queryset = Servico.objects.all()
