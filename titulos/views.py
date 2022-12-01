from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Titulo
# Create your views here.


def index(request):
    titulos = Titulo.objects.all()
    paginator= Paginator(titulos,4)
    page= request.GET.get('p')
    titulos= paginator.get_page(page)
    return render(request, 'titulos/index.html', {
        'titulo': titulos })

def specs(request,titulo_id ):
    titulos= Titulo.objects.get(id=titulo_id)

    return render(request,'titulos/specs.html',{'titulo':titulos})