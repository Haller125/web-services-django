import requests
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

from payapp.forms import PaymentForm, RequestForm
from payapp.models import Transaction
from register.decorators import admin_required
from register.models import User
from timestampclient import get_thrift_timestamp


# Create your views here.
@transaction.atomic
@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            amount = form.cleaned_data['amount']

            try:
                recipient = User.objects.get(email=recipient_email)
            except User.DoesNotExist:
                return HttpResponseNotFound("Recipient does not exist.")

            if recipient == request.user:
                return HttpResponseForbidden("Cannot send money to yourself.")

            if request.user.balance < amount:
                return HttpResponseForbidden("Insufficient funds.")

            try:
                response = requests.get(
                    f'http://localhost:8000/webapps2025/conversion/{request.user.currency}/{recipient.currency}/{amount}'
                )
                response.raise_for_status()
                converted_amount = response.json()['converted']
            except Exception:
                return HttpResponseServerError("Currency conversion failed.")

            timestamp = get_thrift_timestamp()

            request.user.balance -= amount
            recipient.balance += converted_amount
            request.user.save()
            recipient.save()

            Transaction.objects.create(
                sender=request.user,
                recipient=recipient,
                amount=amount,
                currency=request.user.currency,
                timestamp=timestamp,
                transaction_type="PAYMENT",
                status="COMPLETED"
            )
            return redirect('payapp:transactions')
    else:
        form = PaymentForm()

    return render(request, 'payapp/make_payment.html', {'form': form, 'user': request.user})


@login_required
def transactions_view(request):
    transactions = Transaction.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
    return render(request, 'payapp/transactions.html', {'transactions': transactions, 'user': request.user})

@login_required
def make_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            amount = form.cleaned_data['amount']

            try:
                recipient = User.objects.get(email=recipient_email)
            except User.DoesNotExist:
                return HttpResponseNotFound("Recipient does not exist.")

            if recipient == request.user:
                return HttpResponseForbidden("Cannot request money from yourself.")

            timestamp = get_thrift_timestamp()

            Transaction.objects.create(
                sender=request.user,
                recipient=recipient,
                amount=amount,
                currency=request.user.currency,
                timestamp=timestamp,
                transaction_type="REQUEST",
                status="PENDING"
            )
            return redirect('payapp:transactions')
    else:
        form = RequestForm()

    return render(request, 'payapp/make_request.html', {'form': form, 'user': request.user})
@login_required
def requests_view(request):
    requested_transactions = Transaction.objects.filter(recipient=request.user, status="PENDING")
    return render(request, 'payapp/requests.html', {'requests': requested_transactions, 'user': request.user})

@transaction.atomic
@login_required
def accept_request(request, id):
    if request.method == 'POST':
        requested_transaction = get_object_or_404(
            Transaction,
            id=id,
            recipient=request.user,
            status='PENDING',
            transaction_type='REQUEST'
        )

        try:
            response = requests.get(
                f'http://localhost:8000/webapps2025/conversion/'
                f'{requested_transaction.currency}/{request.user.currency}/{requested_transaction.amount}'
            )
            response.raise_for_status()
            converted_amount = response.json()['converted']
        except Exception:
            return HttpResponseServerError("Currency conversion failed.")

        if request.user.balance < converted_amount:
            return HttpResponseForbidden("Insufficient funds.")

        request.user.balance -= converted_amount
        requested_transaction.sender.balance += requested_transaction.amount
        request.user.save()
        requested_transaction.sender.save()

        requested_transaction.status = 'COMPLETED'
        requested_transaction.transaction_type = 'PAYMENT'
        requested_transaction.timestamp = get_thrift_timestamp()
        requested_transaction.save()

        return redirect('payapp:requests')

@login_required
def reject_request(request, id):
    if request.method == 'POST':
        requested_transaction = get_object_or_404(Transaction, id=id, recipient=request.user, status='PENDING', transaction_type='REQUEST')
        requested_transaction.status = 'REJECTED'
        requested_transaction.timestamp = get_thrift_timestamp()
        requested_transaction.save()
        return redirect('payapp:requests')

@admin_required
def all_transactions_view(request):
    transactions = Transaction.objects.all()
    return render(request, 'payapp/all_transactions.html', {'transactions': transactions})
