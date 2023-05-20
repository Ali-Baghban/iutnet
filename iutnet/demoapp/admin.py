from django.contrib import admin
from .models import AiModel, Dataset, Paper

admin.site.register(Paper)
admin.site.register(Dataset)
admin.site.register(AiModel)
