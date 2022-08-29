from django.shortcuts import render

def pricing(request):
    return render(request, 'payment/pricing.html')
