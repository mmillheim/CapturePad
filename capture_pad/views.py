from django.shortcuts import render

# Create your views here.
from .models import User, Notebook, Year, Month, Day, Note

def notebook_list(request):
    notebooks = Notebook.objects.all()
    return render(request, 'capture_pad/notebook_list.html', {'notebooks': notebooks})

def year_list(request):
    years = Year.objects.all()
    return render(request, 'capture_pad/year_list.html', {'years': years})

def month_list(request):
    months = Month.objects.all()
    return render(request, 'capture_pad/month_list.html', {'months': months})

def day_list(request):
    days = Day.objects.all()
    return render(request, 'capture_pad/day_list.html', {'days': days})

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'capture_pad/note_list.html', {'notes': notes})

def notebook_detail(request, pk):
    notebook = Notebook.objects.get(id=pk)
    return render(request, 'capture_pad/notebook_detail.html', {'notebook': notebook})

def year_detail(request, pk):
    year = Year.objects.get(id=pk)
    return render(request, 'capture_pad/year_detail.html', {'year': year})

def month_detail(request, pk):
    month = Month.objects.get(id=pk)
    return render(request, 'capture_pad/month_detail.html', {'month': month})

def day_detail(request, pk):
    day = Day.objects.get(id=pk)
    return render(request, 'capture_pad/day_detail.html', {'day': day})

def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'capture_pad/note_detail.html', {'note': note})


