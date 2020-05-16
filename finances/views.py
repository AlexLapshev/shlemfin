from django.http import HttpResponse
from django.shortcuts import render

from .models import BaseFinance, Outerwear, Other, Debt, Product
from .forms import OuterwearForm, OtherForm, DebtForm


def finances(request):
	if request.method == 'POST':
		product = Outerwear.objects.filter(pk=int(request.POST['product'])).first()
		price = request.POST['price']
		size = request.POST['size']
		opt_info = request.POST['optional_info']
		optional_info = '{} {} {}'.format(product.name, size.upper(), opt_info)

		finance = BaseFinance(
			price=price,
			optional_info=optional_info,
		)
		finance.save()
		new_q = getattr(product, size)-1
		setattr(product, size, new_q)
		product.quantity = sum([product.s, product.m, product.l, product.xl, product.xxl])
		product.save()
		return HttpResponse('')

	all_operations = BaseFinance.objects.all()
	all_other = Other.objects.all()
	all_outerwear = Outerwear.all_outer_wear()

	debts = Debt.objects.all()
	total = 0
	for i in all_operations:
		if i.operation:
			total += i.price
		else:
			total -= i.price
	total_debt = sum([i.value for i in debts])
	form = OuterwearForm()
	form_other = OtherForm()
	form_debt = DebtForm()

	return render(request, 'finances/finances.html', {'all_operations': all_operations,
													  'all_outerwear': all_outerwear,
													  'all_other': all_other,
													  'total': total,
													  'debts': debts,
													  'total_debt': total_debt,
													  'form': form,
													  'form_other':form_other,
													  'form_debt':form_debt
													  })
