from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from .serializers import NotebookSerializer, YearSerializer, MonthSerializer, DaySerializer, NoteSerializer

# Create your views here.
from .models import User, Notebook, Year, Month, Day, Note

from .forms import NotebookForm, YearForm, MonthForm, DayForm, NoteForm

# list views

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

# detail views

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

# create veiws

def notebook_create(request):
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            notebook = form.save()
            return redirect('notebook_detail', pk=notebook.pk)
    else:
        form = NotebookForm()
    return render(request, 'capture_pad/notebook_form.html', {'form': form})

def year_create(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.save()
            return redirect('year_detail', pk=year.pk)
    else:
        form = YearForm()
    return render(request, 'capture_pad/year_form.html', {'form': form})

def month_create(request):
    if request.method == 'POST':
        form = MonthForm(request.POST)
        if form.is_valid():
            month = form.save()
            return redirect('month_detail', pk=month.pk)
    else:
        form = MonthForm()
    return render(request, 'capture_pad/month_form.html', {'form': form})

def day_create(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            day = form.save()
            return redirect('day_detail', pk=day.pk)
    else:
        form = DayForm()
    return render(request, 'capture_pad/day_form.html', {'form': form})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'capture_pad/note_form.html', {'form': form})


# edit views
def notebook_edit(request, pk):
    notebook = Notebook.objects.get(pk=pk)
    if request.method == "POST":
        form = NotebookForm(request.POST, instance=notebook)
        if form.is_valid():
            notebook = form.save()
            return redirect('notebook_detail', pk=notebook.pk)
    else:
        form = NotebookForm(instance=notebook)
    return render(request, 'capture_pad/notebook_form.html', {'form': form})

def year_edit(request, pk):
    year = Year.objects.get(pk=pk)
    
    if request.method == "POST":
        form = YearForm(request.POST, instance=year)
        if form.is_valid():
            year = form.save()
            return redirect('year_detail', pk=year.pk)
    else:
        form = YearForm(instance=year)
    return render(request, 'capture_pad/year_form.html', {'form': form})

def month_edit(request, pk):
    month = Month.objects.get(pk=pk)

    if request.method == "POST":
        form = MonthForm(request.POST, instance=month)
        if form.is_valid():
            month = form.save()
            return redirect('month_detail', pk=month.pk)
    else:
        form = MonthForm(instance=month)
    return render(request, 'capture_pad/month_form.html', {'form': form})

def day_edit(request, pk):
    day = Day.objects.get(pk=pk)
    if request.method == "POST":
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            day = form.save()
            return redirect('day_detail', pk=day.pk)
    else:
        form = DayForm(instance=day)
    return render(request, 'capture_pad/day_form.html', {'form': form})

def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'capture_pad/note_form.html', {'form': form})

# delete

def notebook_delete(request, pk):
    Notebook.objects.get(id=pk).delete()
    return redirect('notebook_list')

def year_delete(request, pk):
    Year.objects.get(id=pk).delete()
    return redirect('year_list')

def month_delete(request, pk):
    Month.objects.get(id=pk).delete()
    return redirect('month_list')

def day_delete(request, pk):
    Day.objects.get(id=pk).delete()
    return redirect('day_list')

def note_delete(request, pk):
    Note.objects.get(id=pk).delete()
    return redirect('note_list')


##API

#Notebooks
class NotebookList(generics.ListCreateAPIView):
    queryset = Notebook.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NotebookSerializer

class NotebookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notebook.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NotebookSerializer

#Years
class YearList(generics.ListCreateAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class YearDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

#Months
class MonthList(generics.ListCreateAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

class MonthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

#Days
class DayList(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

#Notes
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer