from django.http import HttpResponse
from django.shortcuts import render

from .models import BaseFinance, Product, Debt
from .forms import BaseFinanceForm


def finances(request):
	if request.method == 'POST':
		product = Product.objects.filter(pk=int(request.POST['product'])).first()
		value = request.POST['value']
		title = request.POST['title']
		operation = request.POST['operation']
		product.quanity -= 1
		if product.quanity == 0:
			product.available = False
		finance = BaseFinance(
			product=product,
			value=value,
			title=title,
			operation=operation
		)
		finance.save()
		product.save()
		return HttpResponse('')

	all_operations = BaseFinance.objects.all()
	all_products = Product.objects.all()
	debts = Debt.objects.all()
	total = 0
	for i in all_operations:
		if i.operation:
			total += i.value
		else:
			total -= i.value
	total_debt = sum([i.value for i in debts])
	form = BaseFinanceForm()
	return render(request, 'finances/finances.html', {'all_operations': all_operations,
													  'all_products': all_products,
													  'total': total,
													  'debts': debts,
													  'total_debt': total_debt,
													  'form': form})
