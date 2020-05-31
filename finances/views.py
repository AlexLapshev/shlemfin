from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


from .models import BaseFinance, Debt, Product, OuterwearDetail, ProductDetail, Size, OtherDetail, SendTo
from .forms import BaseFinanceForm, SendToForm
from django.db.models import Sum


@csrf_exempt
def finances(request):
    if request.method == 'POST':
        form = BaseFinanceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_f = BaseFinance()
            new_f.product = data['product']
            new_f.price = data['price']
            new_f.operation = data['operation']
            new_f.optional_info = '{}'.format(data['optional_info'])
            print(data['size'])
            if data['size'] != 'False':
                new_f.optional_info = '{} {}'.format(data['size'], data['optional_info'])
                size_id = Size.objects.filter(name=data['size']).first().pk
                product = OuterwearDetail.objects.filter(product=data['product'], size__pk=size_id).first()
                product.quantity_size -= 1
                product.check_available(product.quantity_size)
                prod_total_q = Product.objects.filter(pk=request.POST['product']).first()
                prod_total_q.quantity = OuterwearDetail.total_quantity(request.POST['product'])
                prod_total_q.check_av()
                prod_total_q.save()
            else:
                product = Product.objects.filter(pk=request.POST['product']).first()
                product.check_av()
                product.quantity -= 1
            product.save()
            new_f.save()
            return HttpResponse('')

    form = BaseFinanceForm()
    send_to_form = SendToForm()
    context = {
        'form': form,
        'products': Product.objects.all(),
        'all_sizes': OuterwearDetail.all_sizes(),
        'all_finances': BaseFinance.all_finances(),
        'total': BaseFinance.total_money(),
        'all_debts': Debt.objects.all(),
        'total_debts': Debt.objects.aggregate(Sum('value')),
        'all_outer': OuterwearDetail.all_outer(),
        'all_other': OtherDetail.objects.all(),
        'send_to_form': send_to_form,
        'all_send_to':SendTo.objects.all()
    }

    return render(request, 'finances/finances.html', context)


@require_http_methods(["POST"])
@csrf_exempt
def send_to(request):
    print(request.POST)
    if request.method == 'POST':
        form = SendToForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_info = SendTo()
            send_info.fcs = data['fcs']
            send_info.where = data['where']
            send_info.send_description = data['send_description']
            send_info.save()
            return HttpResponse('OK')

