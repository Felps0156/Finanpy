from django.shortcuts import render


def home(request):
    """Renderiza um template simples para validar estrutura de templates."""
    return render(request, 'core/home.html')
