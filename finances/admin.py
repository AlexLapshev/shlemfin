from django.contrib import admin

from .models import BaseFinance, Size, Tshirt, Longsleeve, Tape, Debt

admin.site.register(BaseFinance)
admin.site.register(Size)
admin.site.register(Tshirt)
admin.site.register(Longsleeve)
admin.site.register(Tape)
admin.site.register(Debt)


