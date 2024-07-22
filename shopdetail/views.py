from django.shortcuts import render


def shop_detail_view(request):
    return render(request, 'product.html')
