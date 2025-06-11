from django.shortcuts import render
from django.contrib import messages
from asilmedia.models import Media

def home(request):
    kino = Media.objects.all()
    messages.success(request, "Siz bosh sahifaga keldingiz")
    multfilmlar = Media.objects.filter(categorykinolar__categorykino__iexact='Multfilmlar')
    hindkinolar = Media.objects.filter(categorykinolar__categorykino__iexact='Hind Kinosi')
    premyeralar = Media.objects.filter(categorykinolar__categorykino__iexact='Premyera')
    tarjimakinolar = Media.objects.filter(categorykinolar__categorykino__iexact='Tarjima Kinolar')
    
    return render(request, 'home.html', {'kino': kino, 'multfilmlar': multfilmlar,  'hindkinolar': hindkinolar, 'premyeralar': premyeralar, 'tarjimakinolar': tarjimakinolar })

def videoPage(request):
    return render(request, 'video_page.html')