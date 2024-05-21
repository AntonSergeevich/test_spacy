from django.shortcuts import render
from .models import SlideImg


# Create your views here.
def index(request):
    model_image = SlideImg.objects.all()
    context = {'model_image': model_image}
    return render(request, 'space/index.html', context)