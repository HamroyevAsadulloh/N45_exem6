from django.shortcuts import render


def client_view(request):
    return render(request, 'xaridlar.html')