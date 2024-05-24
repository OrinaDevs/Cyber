from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    current_year = datetime.now().year
    context = {
        'year': current_year,
    }

    return render(request, 'index.html', context)

def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())
    