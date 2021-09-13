from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Notebook(models.Model):
    title = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebooks')
    
    def __str__(self):
        return self.title

class Year(models.Model):
    name = models.IntegerField(default=2021)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='years')

    def __str__(self):
        return str(self.name)

class Month(models.Model):
    name = models.CharField(default='name of month', max_length=100)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='months')

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='days')

    def __str__(self):
        return str(self.name)

class Note(models.Model):
    textContent = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    dueDate = models.DateField(null=True, blank=True)

    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.textContent