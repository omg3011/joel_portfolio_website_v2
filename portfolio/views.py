from django.shortcuts import render, get_object_or_404
from .models import CategoryModel

# Create your views here.
def categories(request):
    categoryModels = CategoryModel.objects.all()
    return render(request, 'portfolio/categories.html', {"categories":categoryModels})
