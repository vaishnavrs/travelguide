from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Place,Team

# Create your views here.
def index(request):
    place_obj=Place.objects.all()
    team_obj=Team.objects.all()
    return render(request, "index.html",{'place_key':place_obj,'teams':team_obj})

# def TeamView(request):
#     team_obj=Team.objects.all()
#     return render(request,"index.html",{"teams":team_obj})