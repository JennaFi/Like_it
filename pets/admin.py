from django.contrib import admin
from .models import Pet, PetAdmin

admin.site.register(Pet, PetAdmin)

