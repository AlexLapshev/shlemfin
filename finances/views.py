from django.shortcuts import render
from .models import BaseFinance, Product, Debt


def finances(request):
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
	print(total_debt)
	return render(request, 'finances/finances.html', {'all_operations': all_operations,
													  'all_products': all_products,
													  'total': total,
													  'debts': debts,
													  'total_debt': total_debt})
