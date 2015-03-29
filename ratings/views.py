from django.shortcuts import render, get_object_or_404
from .models import Category
from .models import Tool
from .models import ToolCat

# Create your views here.

def categorys_list(request):
    categorys = Category.objects.all()
    return render(request, 'ratings/categorys_list.html', {'categorys': categorys})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    tools = Tool.objects.filter(toolcat__cat_id = category)
    return render(
            request, 
            'ratings/category_detail.html', 
            {'category': category, 'tools':tools})
