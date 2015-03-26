from django.shortcuts import render, get_object_or_404
from .models import Category
from .models import Tool

# Create your views here.

def categorys_list(request):
    categorys = Category.objects.all()
    return render(request, 'ratings/categorys_list.html', {'categorys': categorys})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'ratings/category_detail.html', {'category': category})
