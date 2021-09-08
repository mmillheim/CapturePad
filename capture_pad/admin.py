from django.contrib import admin
from .models import User, Notebook, Year, Month, Day, Note

admin.site.register(User)
admin.site.register(Notebook)
admin.site.register(Year) 
admin.site.register(Month) 
admin.site.register(Day) 
admin.site.register(Note)

# Register your models here.
