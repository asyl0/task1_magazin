from django.shortcuts import render
from .models import Food

def foods_page(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }

    return render(request, "./foods_page.html", context)
