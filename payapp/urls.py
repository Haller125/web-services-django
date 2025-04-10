from django.urls import path
from .views import transactions_view, make_payment, make_request, requests_view, accept_request, reject_request, all_transactions_view

app_name = 'payapp'

urlpatterns = [
    path('transactions/', transactions_view, name='transactions'),
    path('make_payment/', make_payment, name='make_payment'),
    path('make_request/', make_request, name='make_request'),
    path('requests/', requests_view, name='requests'),
    path('accept-request/<int:id>/', accept_request, name='accept_request'),
    path('reject-request/<int:id>/', reject_request, name='reject_request'),
    path('all_transactions/', all_transactions_view, name='all_transactions'),
]
