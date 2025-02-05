from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import DVD, VHS, VideoEquipments
from catalogo.forms import DVDForm, VHSForm, VideoEquipmentsForm

def index(request):
    dvds = DVD.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {
            'dvds':dvds,
        },
        request))

def VHSs(request):
    VHSs = VHS.objects.all()
    template = loader.get_template('client_list.html')
    return HttpResponse(template.render(
        {
            'vhss':VHSs,
        },
        request))

def Video_Equipments(request, VideoEquipments_id):
    videoEquipments = VideoEquipments.objects.get(id=VideoEquipments_id)
    template = loader.get_template('display_client.html')
    context = {
        'videoequipments': videoEquipments
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_DVD(request):
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

def edit_DVD(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES, instance=dvd)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm(instance=dvd)
    
    return render(request, 'dvd_form.html', {'form': form})

def delete_DVD(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    dvd.delete()
    return redirect('catalogo:index')

class CustomLoginView(LoginView):
    template_name = "login_form.html"