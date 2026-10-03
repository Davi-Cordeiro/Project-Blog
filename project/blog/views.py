from django.shortcuts import render
from site_setup.views import get_site_setup_context

# Create your views here.

def index(request): 
    return render(request, 'blog/pages/index.html', get_site_setup_context(request))