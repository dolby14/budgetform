from django.contrib import admin

# Register your models here.
from budget_extension.models import Extension, Research_fellow, Material, Other

admin.site.register(Extension)

admin.site.register(Research_fellow)

admin.site.register(Material)

admin.site.register(Other)