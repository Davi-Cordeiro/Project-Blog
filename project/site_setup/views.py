from django.shortcuts import render
from site_setup.models import SiteSetup

def get_site_setup_context(request):
    dados = SiteSetup.objects.first()
    return {
        'site_setup': {
            'title': dados.title if dados else 'Nenhum título definido',
        }
    }