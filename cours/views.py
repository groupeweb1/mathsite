from django.shortcuts import render
from .models import Lecon

def lecon(request):
    query = request.GET.get("q")

    if query:
        data = Lecon.objects.filter(question__icontains=query)
    else:
        data = Lecon.objects.all()

    return render(request, "home.html", {"home": data})
def home(request):
    return render(request, "cours/home.html")