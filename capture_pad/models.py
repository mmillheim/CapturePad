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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebooks')
    
    def __str__(self):
        return self.title

class Year(models.Model):
    name = models.IntegerField
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name='years')

    def __str__(self):
        return self.name

class Month(models.Model):
    name = models.IntegerField
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='months')

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.IntegerField
    date = models.DateField
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='days')

    def __str__(self):
        return self.name

class Note(models.Model):
    textContent = models.TextField
    complete = models.BooleanField(default=False)
    date = models.DateField
    dueDate = models.DateField

    month = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.textContent