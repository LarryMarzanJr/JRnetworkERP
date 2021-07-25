from django.shortcuts import render

# Create your views here.

def adminlte_view(request):
    return render(request, "adminlte_testing/starter.html", {})