from django.contrib import admin

# Register your models here.

# Import pet model from models.py
from .models import Pet

# Register this class with the admin to tell it which model it's associated with.
# Menggunakan decorator (decorator itu @ apa gitu)
@admin.register(Pet)
# Create admin interface for Pet model -> with using class
class PetAdmin(admin.ModelAdmin):
    
    # The list_display is attribute that ModelAdmin class has. 
    # It allow to define which fields are displayed on listign screen
    # Just like this, the fields in Pets (web) change.
    list_display = ['name', 'species', 'breed', 'age', 'sex']