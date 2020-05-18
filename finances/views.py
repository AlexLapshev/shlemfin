from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import BaseFinance, Debt, Product, OuterwearDetail, ProductDetail, Size, OtherDetail
from .forms import BaseFinanceForm


# from .forms import OuterwearForm, OtherForm, DebtForm


# def finances(request):
# 	if request.method == 'POST':
# 		product = Outerwear.objects.filter(pk=int(request.POST['product'])).first()
# 		price = request.POST['price']
# 		size = request.POST['size']
# 		opt_info = request.POST['optional_info']
# 		optional_info = '{} {} {}'.format(product.name, size.upper(), opt_info)
#
# 		finance = BaseFinance(
# 			price=price,
# 			optional_info=optional_info,
# 		)
# 		finance.save()
# 		new_q = getattr(product, size)-1
# 		setattr(product, size, new_q)
# 		product.quantity = sum([product.s, product.m, product.l, product.xl, product.xxl])
# 		product.save()
# 		return HttpResponse('')
#
# 	all_operations = BaseFinance.objects.all()
# 	all_other = Other.objects.all()
# 	all_outerwear = Outerwear.all_outer_wear()
#
# 	debts = Debt.objects.all()
# 	total = 0
# 	for i in all_operations:
# 		if i.operation:
# 			total += i.price
# 		else:
# 			total -= i.price
# 	total_debt = sum([i.value for i in debts])
# 	form = OuterwearForm()
# 	form_other = OtherForm()
# 	form_debt = DebtForm()
#
# 	return render(request, 'finances/finances.html', {'all_operations': all_operations,
# 													  'all_outerwear': all_outerwear,
# 													  'all_other': all_other,
# 													  'total': total,
# 													  'debts': debts,
# 													  'total_debt': total_debt,
# 													  'form': form,
# 													  'form_other':form_other,
# 													  'form_debt':form_debt
# 													  })
# 	return HttpResponse('OK')

@csrf_exempt
def finances(request):
	if request.method == 'POST':
		print(request.POST)
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
				print(request.POST)
				product = Product.objects.filter(pk=request.POST['product']).first()
				product.check_av()
				product.quantity -= 1
				print(product)
			product.save()
			new_f.save()
			return HttpResponse('')

	form = BaseFinanceForm()
	context = {
		'form': form,
		'products': Product.objects.all(),
		'all_sizes': OuterwearDetail.all_sizes(),
		'all_finances': BaseFinance.all_finances(),
		'total': BaseFinance.total_money(),
		'all_debts': Debt.objects.all(),
		'all_outer': OuterwearDetail.all_outer(),
		'all_other': OtherDetail.objects.all()
	}

	return render(request, 'finances/finances1.html', context)
