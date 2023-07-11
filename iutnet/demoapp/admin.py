from django.contrib import admin
from .models import AiModel, Dataset, Paper, Request

class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name','type','private','ready_to_use')
    """list_display_links = ('title', 'city', 'realtor','price')
    list_editable = ('is_published', 'is_best_deal')
    list_filter = ('is_published','city', 'is_best_deal')
    search_fields = ('title','realtor','price','bedrooms','bathrooms')
    list_per_page = 25"""

admin.site.register(Paper)
admin.site.register(Dataset, DatasetAdmin)
admin.site.register(AiModel)
admin.site.register(Request)
