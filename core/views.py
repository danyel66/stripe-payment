from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = "sk_test_co8XAgMCIPF7uAFZ9O5pWU2I00hX8N3CuH"

def index(request):
    return render(request, 'core/index.html')

def charge(request):
    amount = int(request.POST['amount1'])
    if request.method == 'POST':
        print('Data:', request.POST)

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency="NGN",
            description="My First Test Charge (created for API docs)",
            )

    return redirect(reverse('success', args=[amount]))

def success(request, args):
    amount = args
    return render(request, 'core/success.html', {'amount': amount})
