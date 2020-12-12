from django.shortcuts import render, get_object_or_404
from .models import AboutModel

# Create your views here.
def about_me(request):
    aboutModel = get_object_or_404(AboutModel)
    return render(request, 'about/about.html', {"about":aboutModel})
